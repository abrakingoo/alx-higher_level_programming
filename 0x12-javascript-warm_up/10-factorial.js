#!/usr/bin/node

function factorial (value) {
  if (isNaN(value) || value === 0) {
    return 1;
  } else {
    return value * factorial(value - 1);
  }
}

const number = parseInt(process.argv[2], 10);
const res = factorial(number);
console.log(res);
