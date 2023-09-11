#!/usr/bin/node

const value = process.argv[2];

if (Number.isNaN(Number(value))) {
  console.log('Missing size');
} else {
  const number = parseInt(value, 10);
  for (let i = 0; i < number; i++) {
    let row = '';
    for (let j = 0; j < number; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
