const fs = require('fs');
let [hour, min] = fs.readFileSync("/dev/stdin").toString().trim().split(" ");

hour = Number(hour);
min = Number(min);


if (min >= 45) {console.log(hour, min-45);}
else {
    if (hour === 0) {hour = 24;}
    console.log(hour-1,min+15);}