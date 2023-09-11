#!/usr/bin/node
// Call me Moby
exports.callMeMoby = (x, theFunction) => {
  for (let i = 0; i < x; i++) theFunction();
};
