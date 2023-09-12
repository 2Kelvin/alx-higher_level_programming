#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let elementCount = 0;
  list.forEach(el => {
    if (el === searchElement) {
      elementCount++;
    }
  });
  return elementCount;
};
