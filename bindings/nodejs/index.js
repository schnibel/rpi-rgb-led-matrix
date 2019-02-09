//index.js
const nodejs_binding = require('./build/Release/rpi_rgb_led_matrix_nodejs.node');

console.log("Let's go....");
console.log('addon',nodejs_binding);
console.log('say Hello = ', nodejs_binding.hello());
console.log("add 5 to 6 = ", nodejs_binding.add(5, 6));

const classInstance = new nodejs_binding.ClassExample(4.3);
console.log('Testing class initial value : ',classInstance.getValue());
console.log('After adding 3.3 : ',classInstance.add(3.3));
module.exports = nodejs_binding;