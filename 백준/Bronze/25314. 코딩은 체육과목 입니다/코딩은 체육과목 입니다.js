const fs = require('fs');
let input = parseInt(fs.readFileSync("/dev/stdin").toString().trim());

for(let i=0; i<input; i=i+4){
    process.stdout.write('long ');
}
console.log('int');