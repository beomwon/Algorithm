const fs = require('fs');
const input = Number(fs.readFileSync("/dev/stdin").toString().trim());
process.stdout.write('long '.repeat(parseInt(input/4)));
console.log('int');