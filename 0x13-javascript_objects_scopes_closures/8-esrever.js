#!/usr/bin/node
exports.esrever = function (list) {
  const reverseList = [];
  let lastIdx = list.length - 1;

  list.forEach(item => {
    reverseList[lastIdx] = item;
    lastIdx--;
  });
  return reverseList;
};
