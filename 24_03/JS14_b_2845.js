// let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
let input = require('fs').readFileSync('../temp/input.txt').toString().split('\n');

var [L, P] = input[0].split(' ').map(Number);
var people = L * P;
var news = input[1].split(' ').map(Number);
var result = '';

for (let i = 0; i < 5; i++) {
    result += (news[i] - people) + ' '
}

console.log(result)