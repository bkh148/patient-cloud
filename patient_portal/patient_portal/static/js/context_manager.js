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

		socket.on('on_load', function () {
		});

		socket.on('on_send', function (data) {
			handle_data_received(data);
		});

		socket.on('on_user_login', function (data) {
			context_manager._cache['online_users'][data['user_id']] = data['user_sid']
			user_logged_in(data);
		});

		socket.on('on_user_logout', function (data) {
			delete context_manager._cache['online_users'][data['user_id']];
			user_logged_out(data);
		});

	} catch (err) {
		context_manager.post_exception('CLIENT_EXCEPTION_CONTEXT_MANAGER', err);
        context_manager.error_message(`An unexpected error has occurred whilst loading your dashboard, please try refreshing the page.`);
	}
}

ContextManager.prototype.logout = function () {
	try {
		socket.emit('logout', {});
		context_manager.post_activity('CONTEXT_MANAGER_LOGOUT');
	} catch (err) {
		context_manager.post_exception('CLIENT_EXCEPTION_CONTEXT_MANAGER', err);
        context_manager.error_message(`An unexpected error has occurred whilst logging your out..`);
	}
}

ContextManager.prototype.format_name = function (name) {
	return name.charAt(0).toUpperCase() + name.slice(1).toLowerCase();
}


ContextManager.prototype.new_guid = function () {
	return ([1e7] + -1e3 + -4e3 + -8e3 + -1e11).replace(/[018]/g, c =>
		(c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16)
	);
}

let create_notification = function (type, icon, message, options, time = null, title_override = null) {
	let notification = document.createElement('div');
	$(notification).attr('class', `toast toast-${type}`);
	$(notification).attr('role', 'alert');
	$(notification).attr('aria-live', 'assertive');
	$(notification).attr('aria-atomic', 'true');
	$(notification).html(context_manager._cache.templates["notification"]);

	let notification_icon = $(notification).find('#toast-icon');
	$(notification_icon).attr('class', `${icon} mr-2`);

	let notification_title = $(notification).find('#toast-title');
	if (title_override != null) {
		$(notification_title).html(context_manager.format_name(title_override));
	} else {
		$(notification_title).html(context_manager.format_name(type));
	}

	let notification_time = $(notification).find('#notification-time');
	if (time == null) {
		$(notification_time).html('just now');
	} else {
		$(notification_time).html('TODO');
	}

	let notification_body = $(notification).find('#notification-body');
	$(notification_body).html(message);
	$(notification).appendTo('#notification-wrapper');

	return notification
}

ContextManager.prototype.update_component = function(name) {
	let component = undefined;
	for (let i = 0; i < context_manager.components.length; i++) {
		component = context_manager.components[i];

		if (component.name == name) {
			component.hide();
			component.show();
			break;
		}
	}
}

ContextManager.prototype.success_message = function (message, time = null) {
	let notification = create_notification('success', 'far fa-check-circle', message, options = { delay: 3500 }, time = time);

	$(notification).toast(options);
	$(notification).toast('show');
}

ContextManager.prototype.error_message = function (message, time = null) {
	let notification = create_notification('error', 'far fa-times-circle', message, options = { delay: 3500 }, time = time);

	$(notification).toast(options);
	$(notification).toast('show');
}

ContextManager.prototype.info_message = function (message, time = null) {
	let notification = create_notification('information', 'far fa-question-circle', message, options = { delay: 3500 }, time = time);

	$(notification).toast(options);
	$(notification).toast('show');
	$(notification).on('hide', function() {
		console.log('hidden');
	})
}

ContextManager.prototype.binary_prompt = function (id, title, message, positive_value, callback_positive, negative_value, callback_negative) {
	if (document.getElementById(`notification_${id}`) == null) {
		let notification_id = id;
		let binary_markdown = `
		<div class="container-fluid">
			<div class="row">
				${message}
			</div>
			<div class="row justify-content-end">
				<div id="notification_negative_${notification_id}" class="btn btn-danger m-2">${context_manager.format_name(negative_value)}</div>
				<div id="notification_positive_${notification_id}" class="btn btn-success m-2">${context_manager.format_name(positive_value)}</div>
			</div>
		</div>
		`;

		let body_wrapper = document.createElement('div');
		$(body_wrapper).html(binary_markdown);

		let notification = create_notification('warning', 'far fa-question-circle', binary_markdown, options = { autohide: false }, time = null, title_override = title);
		$(notification).attr('id', `notification_${notification_id}`);

		let close_button = $(notification).find('#close-notification');
		$(close_button).attr('id', `${close_button.attr('id')}_${notification_id}`);
		$(close_button).on('click', function () {
			if (callback_negative != null) {
				callback_negative();
			}
			$(notification).remove();
		})

		let negative_button = $(notification).find(`#notification_negative_${notification_id}`);
		$(negative_button).on('click', function () {
			if (callback_negative != null) {
				callback_negative();
			}
			$(notification).toast('hide');
			$(notification).remove();
		})

		let positive_button = $(notification).find(`#notification_positive_${notification_id}`);
		$(positive_button).on('click', function () {
			callback_positive();
			$(notification).toast('hide');
			$(notification).remove();
		});

		$(notification).toast(options);
		$(notification).toast('show');
	}
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
			beforeSend: function (request) {
				request.setRequestHeader("Authorization", `Bearer ${context_manager._cache.configurations['access_token']}`);
			},
			contentType: "application/json; charset=utf-8",
			data: JSON.stringify(activity),
			error: function (jqXHR, textStatus, errorThrown) {
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
			beforeSend: function (request) {
				request.setRequestHeader("Authorization", `Bearer ${context_manager._cache.configurations['access_token']}`);
			},
			contentType: "application/json; charset=utf-8",
			data: JSON.stringify(exception),
			error: function (jqXHR, textStatus, errorThrown) {
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

			context_manager.post_activity(`CONTEXT_MANAGER_SWITCH_CONTEXT_${target.toUpperCase()}`);
		}
	} catch (err) {
		context_manager.post_exception('CLIENT_EXCEPTION_CONTEXT_MANAGER', err);
        context_manager.error_message(`An unexpected error has occurred whilst loading elements on your dashboard dashboard, please try refreshing the page.`);
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
        context_manager.post_exception('CLIENT_EXCEPTION_CONTEXT_MANAGER', err);
        context_manager.error_message(`An unexpected error has occurred whilst loading your dashboard, please try refreshing the page.`);
	}
	console.log('Context manager initialized successfully.');

});
