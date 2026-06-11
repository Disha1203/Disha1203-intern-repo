// calculator.js
const add = (a, b) => a + b;

const divide = (a, b) => {
  if (b === 0) {
    throw new Error('Cannot divide by zero');
  }
  return a / b;
};

const multiply = (a, b) => a * b;

module.exports = { add, divide, multiply };
