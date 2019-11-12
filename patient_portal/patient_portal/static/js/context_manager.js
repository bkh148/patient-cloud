class ContextManager {
	constructor(cache) {
		this._cache = cache
	}
}

ContextManager.prototype.current_context = 'not_set'
ContextManager.prototype.components = []

ContextManager.prototype.initialise_socket = function() {
	try {
		let socket = io.connect(`http://${this._cache["configurations"]["host"]}:${this._cache["configurations"]["port"]}/${this._cache["configurations"]["namespace"]}`);

		socket.on('connect', function() {
			socket.emit('load_dashboard', {});
		});

	} catch (err) {
		console.log(`Exception occurred whilst setting up socket: ${err}`)
	}
}

ContextManager.prototype.update_sidebar = function(target) {
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

ContextManager.prototype.switch_context = function(target) {
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
	} catch(err) {
		console.log(`An error has occurred whilst switching the context: ${err}`);
	}
}

$(document).ready(function(){

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
	} catch (err) {
		console.log(`An error has occurred whilst loading the context manager: ${err}`);
	}
	 console.log('Context manager initialized successfully.');
	 
});
