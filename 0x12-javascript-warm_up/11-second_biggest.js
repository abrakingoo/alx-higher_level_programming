#!/usr/bin/node

const list = process.argv.slice(2);

const length = list.length;

if (length === 0 || length === 1) {
  console.log(0);
} else {
  const sortedList = list.sort((a, b) => a - b);
  const secondLargestNumber = sortedList[length - 2];
  console.log(secondLargestNumber);
}
