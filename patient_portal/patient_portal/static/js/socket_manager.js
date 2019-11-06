class SocketManager {
	constructor(configurations) {
		this._configurations = configurations
	}
}

SocketManager.prototype.get_configurations = function() {
	console.table(this._configurations)
}

SocketManager.prototype.initialise_socket = function() {
	try {
		let socket = io.connect(`http://${this._configurations["host"]}:${this._configurations["port"]}/${this._configurations["namespace"]}`);

		socket.on('connect', function() {
			socket.emit('load_dashboard', {});
		});

	} catch (err) {
		console.log(`Exception occurred whilst setting up socket: ${err}`)
	}
}


$(document).ready(function(){
	console.log(socket_configurations)
	socket_manager = new SocketManager(socket_configurations)

	socket_manager.initialise_socket()
});
