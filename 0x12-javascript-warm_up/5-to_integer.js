#!/usr/bin/node

const number = process.argv[2];

if (Number.isNaN(Number(number))) {
  console.log('Not a number');
} else {
  const newNumber = parseInt(number, 10);
  console.log(`My number: ${newNumber}`);
}
