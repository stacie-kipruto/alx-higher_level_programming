#!/usr/bin/node
const arr = [];
if ((process.argv.length === 2) || (process.argv.length === 3)) {
  console.log(0);
} else {
  for (let i = 2; i < process.argv.length; i++) {
    arr.push(parseInt(process.argv[i]));
  }
  const max = Math.max(...arr);
  arr.splice(arr.indexOf(max), 1);
  console.log(Math.max(...arr));
}
