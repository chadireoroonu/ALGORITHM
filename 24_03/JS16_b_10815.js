// let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
let input = require('fs').readFileSync('../temp/input.txt').toString().split('\n');

const N = parseInt(input[0]);
// 카드를 저장할 배열
const set = new Set();

// 가지고 있는 카드 정보 Set에 추가
const cards = input[1].split(' ').map(Number);
for (let i = 0; i < N; i++) {
    set.add(cards[i])
}

// 가지고 있는지 확인할 카드 정보
const M = parseInt(input[2]);
const target = input[3].split(' ').map(Number);
let result = '';

// 타겟이 Set에 들어있는지 확인 후 result에 결과 추가
for (let i = 0; i < M; i++) {
    if (set.has(target[i])) {
        result += '1 ';
    }
    else {
        result += '0 ';
    }
}

console.log(result);