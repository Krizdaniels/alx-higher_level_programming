#!/usr/bin/node
// It executes x times a function.

exports.addMeMaybe = function (number, theFunction) {
  number++;
  theFunction(number);
};
