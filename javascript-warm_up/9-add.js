#!/usr/bin/node

first = parseInt(process.argv[2]);
second = parseInt(process.argv[3]);

if (isNaN(first) || isNaN(second)) {
  console.log('NaN');
} else {
  console.log(first + second);
}
