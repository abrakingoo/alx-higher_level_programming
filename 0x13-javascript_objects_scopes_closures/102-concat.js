#!/usr/bin/node

const file1 = process.argv[2];
const file2 = process.argv[3];
const file3 = process.argv[4];
const fs = require('fs');

fs.readFile(file1, function (err, data) {
  let wholeContent = '';
  if (err) {
    return console.error(err);
  }
  wholeContent += data;

  fs.readFile(file2, function (err, data) {
    if (err) {
      return console.error(err);
    }
    wholeContent += data;
    fs.writeFile(file3, wholeContent, function (err) {
      if (err) {
        return console.error(err);
      }
    });
  });
});
