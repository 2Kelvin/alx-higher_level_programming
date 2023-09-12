#!/usr/bin/node
const SquareOne = require('./5-square');

class Square extends SquareOne {
  charPrint (c) {
    if (!c) super.print();
    else {
      for (let ht = 0; ht < this.height; ht++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
