#!/usr/bin/node

const times = process.argv[2];

if (Number.isNaN(Number(times))) {
  console.log('Missing number of occurrences');
} else {
  const number = parseInt(times, 10);
  for (let i = 0; i < number; i++) {
    console.log('C is fun');
  }
}
