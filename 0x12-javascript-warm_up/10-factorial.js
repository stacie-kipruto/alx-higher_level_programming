#!/usr/bin/node
function factorial (num) {
  if (num === 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}

if (isNaN(process.argv[2])) {
  console.log(1);
} else {
  console.log(factorial(parseInt(process.argv[2])));
}
