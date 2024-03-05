const input = Number(require('fs').readFileSync("/dev/stdin").toString().trim());
process.stdout.write('long '.repeat(parseInt(input/4)));
console.log('int');