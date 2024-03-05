let fs = require('fs');
let inputs = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
let add_inputs = 0;

inputs.sort(function(a, b){
    return a-b;
});
for(let i=0; i<inputs.length; i++){
    add_inputs = add_inputs + Number(inputs[i]);
}
const aver = add_inputs/inputs.length;
console.log(aver);
console.log(inputs[2]);