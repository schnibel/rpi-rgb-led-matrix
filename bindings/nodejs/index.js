//index.js
const testAddon = require('./build/Release/testaddon.node');
console.log('addon',testAddon);
console.log('say Hello = ', testAddon.hello());
console.log("add 5 to 6 = ", testAddon.add(5, 6));

const classInstance = new testAddon.ClassExample(4.3);
console.log('Testing class initial value : ',classInstance.getValue());
console.log('After adding 3.3 : ',classInstance.add(3.3));
module.exports = testAddon;