let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');

var i = 0
var vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while (true) {
  var temp = input[i];
  let count = 0;
  i++;
  if (temp == '#') break;
  for (let j = 0; j < temp.length; j++) {
    if (vowel.includes(temp[j])) count++
  }
  console.log(count);
}
