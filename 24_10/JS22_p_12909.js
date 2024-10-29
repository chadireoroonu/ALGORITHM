function solution(s){
    var answer = true;
    let stack = [];
    
    for (i in s) {
        let now = s[i];
        if (now == '(') {
            stack.push(now);
        } else {
            if (stack.length == 0) {
                answer = false;
                break;
            } else {
                stack.pop();
            }
        }
    }
    
    if (stack.length > 0) {
        answer = false;
    }

    return answer;
}