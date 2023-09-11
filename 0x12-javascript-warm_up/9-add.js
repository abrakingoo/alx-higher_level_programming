#!/usr/bin/node

const num1 = parseInt(process.argv[2], 10);
const num2 = parseInt(process.argv[3], 10);

function add (a, b) {
  console.log(a + b);
}

add(num1, num2);
