#!/usr/bin/node

function fact (n) {
  let res = 1;
  for (let i = 1; i <= n; i++) {
    res *= i;
  }
  return res;
}

const n = parseInt(process.argv[2]);

if (isNaN(n)) {
  console.log(1);
} else {
  console.log(fact(n));
}