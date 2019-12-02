class ContextManager {
	constructor(cache) {
		this._cache = cache
	}
}

ContextManager.prototype.current_context = 'not_set'
ContextManager.prototype.components = []

ContextManager.prototype.initialise_socket = function () {
	try {
		// Sets a global socket object
		socket = io.connect(`http://${this._cache["configurations"]["host"]}:${this._cache["configurations"]["port"]}/${this._cache["configurations"]["namespace"]}`);

		socket.on('connect', function () {
			socket.emit('load_dashboard', {});
		});

		socket.on('on_load', function (data) {
			context_manager._cache['online_users'] = data['online_users']
		});

		socket.on('on_user_login', function(data) {
			context_manager._cache['online_users'][data['user_id']] = data['user_sid']
			user_logged_in(data);
		});

		socket.on('on_user_logout', function(data) {
			delete context_manager._cache['online_users'][data['user_id']];
			user_logged_out(data);
		});

	} catch (err) {
		console.log(`Exception occurred whilst setting up socket: ${err}`)
	}
}

ContextManager.prototype.logout = function () {
	try {
		socket.emit('logout', {})
	} catch (err) {
		console.log(`Exception occurred whilst setting up socket: ${err}`)
		// Push error to log api
	}
}

ContextManager.prototype.new_guid = function () {
	return ([1e7]+-1e3+-4e3+-8e3+-1e11).replace(/[018]/g, c =>
		(c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16)
	  );
}

ContextManager.prototype.success_message = function(title, message) {
	toastr.options.closeButton = true;
	toastr.success(message, title);
}

ContextManager.prototype.error_message = function(title, message) {
	toastr.options.closeButton = true;
	toastr.error(message, title);
}

ContextManager.prototype.post_activity = function (activity_type) {
	try {

		let activity = {
			'activity_log_id': context_manager.new_guid(),
			'activity_log_type': activity_type,
			'session_id': context_manager._cache.configurations['session_id'],
			'occurred_on_utc': new Date().toISOString(),
		}

		$.ajax({
			url: `http://${context_manager._cache.configurations['host']}:${context_manager._cache.configurations['port']}/api/v1.0/logs/activities`,
			type: 'POST',
			beforeSend: function(request) {
				request.setRequestHeader("Authorization", `Bearer ${context_manager._cache.configurations['access_token']}`);
			  },
			contentType: "application/json; charset=utf-8",
			data: JSON.stringify(activity),
			error: function(jqXHR, textStatus, errorThrown) {
				throw new Error(errorThrown)
			}
		})
	} catch (err) {
		console.log(`An error has occurred whilst posting activity logs to server: ${err}`)
	}
}

ContextManager.prototype.post_exception = function (type, error) {
	try {
		let exception = {
			'exception_log_id': context_manager.new_guid(),
			'exception_log_type': type,
			'session_id': context_manager._cache.configurations['session_id'],
			'occurred_on_utc': new Date().toISOString(),
			'is_handled': true,
			'stack_trace': error.message
		}

		$.ajax({
			url: `http://${context_manager._cache.configurations['host']}:${context_manager._cache.configurations['port']}/api/v1.0/logs/exceptions`,
			type: 'POST',
			beforeSend: function(request) {
				request.setRequestHeader("Authorization", `Bearer ${context_manager._cache.configurations['access_token']}`);
			  },
			contentType: "application/json; charset=utf-8",
			data: JSON.stringify(exception),
			error: function(jqXHR, textStatus, errorThrown) {
				throw new Error(errorThrown)
			}
		})
	} catch (err) {
		console.log(`An error has occurred whilst posting error logs to server: ${err}`)
	}
}

ContextManager.prototype.update_sidebar = function (target) {
	for (i = 0; i < context_manager._cache.components.length; i++) {
		let component = context_manager._cache.components[i];
		let element = document.getElementById(`sidebar_button_${component}`)

		if (element.classList.contains('active') && target != component) {
			element.classList.remove('active');
		} else if (!element.classList.contains('active') && target == component) {
			element.classList.add('active');
		}
	}
}

ContextManager.prototype.switch_context = function (target) {
	try {
		if (context_manager.current_context != target) {
			// Do switching work

			// If the switch succeeded, change the context and update the sidebar styles
			context_manager.current_context = target;
			context_manager.update_sidebar(target);

			for (i = 0; i < context_manager.components.length; i++) {
				let component = context_manager.components[i];
				if (component.name == target) {
					component.show();
				} else {
					component.hide();
				}
			}

			console.log(`Current context: ${context_manager.current_context}`);
		} else {
			console.info(`Target already in context.`);
		}
	} catch (err) {
		console.log(`An error has occurred whilst switching the context: ${err}`);
		// Push error to log api
	}
}

$(document).ready(function () {

	try {
		context_manager = new ContextManager(metadata);
		let factory = new ComponentFactory();

		// Setup the socket connection with the server
		context_manager.initialise_socket();
		context_manager.current_context = metadata.components[0];

		for (i = 0; i < metadata["components"].length; i++) {
			let component = factory.create_component(metadata["components"][i]);
			context_manager.components.push(component);
		}

		for (i = 0; i < context_manager.components.length; i++) {
			component = context_manager.components[i];
			component.update();
		}

		// Initialise the first component
		context_manager.components[0].show();

	} catch (err) {
		console.log(`An error has occurred whilst loading the context manager: ${err}`);
		// Push error to log api
	}
	console.log('Context manager initialized successfully.');

});
