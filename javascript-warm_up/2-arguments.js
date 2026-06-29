#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length === 0) {
    console.log("no arguments");
} else {
    console.log("Argument found");
}