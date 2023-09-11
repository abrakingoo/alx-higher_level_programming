#!/usr/bin/node

const argc = process.argv.slice(2);

if (argc.length === 1) {
  console.log('Argument found');
} else if (argc.length > 1) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
