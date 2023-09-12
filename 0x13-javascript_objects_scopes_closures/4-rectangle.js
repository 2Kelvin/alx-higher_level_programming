#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let ht = 0; ht < this.height; ht++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const tempH = this.height;
    const tempW = this.width;
    this.height = tempW;
    this.width = tempH;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
}
module.exports = Rectangle;
