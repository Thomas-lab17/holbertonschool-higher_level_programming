#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length === 0) {
  console.log('No arguments');
}
if (args.length === 1) {
  console.log('Argument found');
}
if (args.length > 1) {
  console.log('Arguments found');
}
