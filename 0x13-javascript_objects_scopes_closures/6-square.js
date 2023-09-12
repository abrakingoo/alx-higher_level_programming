#!/usr/bin/node

const SquareBase = require('./5-square');

class Square extends SquareBase {
  constructor (size) {
    super(size);
  }

  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += c;
      }
      console.log(row);
    }
  }
}
module.exports = Square;
