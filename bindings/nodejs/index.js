//index.js
/*
const nodejs_binding = require('./build/Release/rpi_rgb_led_matrix_nodejs.node');

console.log("1 - Let's go....");
//console.log('addon',nodejs_binding);
//console.log('say Hello = ', nodejs_binding.hello());
//console.log("add 5 to 6 = ", nodejs_binding.add(5, 6));

//const classInstance = new nodejs_binding.ClassExample(4.3);
const classInstance = new nodejs_binding.ClassExample(4.3);
console.log('Testing class initial value : ',classInstance.getValue());
console.log('After adding 3.3 : ',classInstance.add(3.3));
module.exports = nodejs_binding;
*/

var ledmatrix = require('./build/Release/rpi_rgb_led_matrix_nodejs.node');

//var ledmatrix = require(path.join(__dirname, "build", "Release", "node-rpi-rgb-led-matrix.node"));
var LedMatrix = ledmatrix.LedMatrix;

/*
LedMatrix.prototype._scroll = LedMatrix.prototype.scroll;
LedMatrix.prototype.scroll = function(params, callback) {
	var startx = params.x >= 0 ? params.x : 0;
	if(startx > this.getWidth()) startx = 0;

	var starty = params.y >= 0 ? params.y : 0;
	if(starty > this.getHeight()) starty = 0;

	var width = params.width >= 0 ? params.width : 0;
	if(width > this.getWidth()) width = this.getWidth();

	var height = params.y >= 0 ? params.height : 0;
	if(height > this.getHeight()) height = this.getHeight();

	var speed = params.speed || 50;
	if(speed <= 0) speed = 50;

	var loop = params.loop || 1;
	if(loop < 0) loop = 1;
	
	var direction = params.direction || LedMatrix.SCROLL_TO_LEFT;
	if(direction != LedMatrix.SCROLL_TO_LEFT && direction != LedMatrix.SCROLL_TO_RIGHT
		&& direction != LedMatrix.SCROLL_TO_TOP && direction != LedMatrix.SCROLL_TO_BOTTOM) {
		direction = LedMatrix.SCROLL_TO_LEFT;
	}

	callback = callback || function(){};

	this._scroll(callback, startx, starty, width, height, direction, speed, loop);
}

LedMatrix.prototype.scroll2Left = function(params, callback) {
	params.direction = LedMatrix.SCROLL_TO_LEFT;
	this.scroll(params, callback);
}

LedMatrix.prototype.scroll2Right = function(params, callback) {
	params.direction = LedMatrix.SCROLL_TO_RIGHT;
	this.scroll(params, callback);
}

LedMatrix.prototype.scroll2Top = function(params, callback) {
	params.direction = LedMatrix.SCROLL_TO_TOP;
	this.scroll(params, callback);
}

LedMatrix.prototype.scroll2Bottom = function(params, callback) {
	params.direction = LedMatrix.SCROLL_TO_BOTTOM;
	this.scroll(params, callback);
}
*/


module.exports = LedMatrix;