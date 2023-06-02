function solution(babbling) {
    let answer = 0;
    for (let i = 0; i < babbling.length; i++) {
        let b = babbling[i];
        let ableList = ['aya', 'ye', 'woo', 'ma'];
        for (let j = 0; j < ableList.length; j++) {
            let able = ableList[j];
            if (b.indexOf(able.repeat(2)) === -1) {
                b = b.replaceAll(able, ' ');
            }
        }
        if (b.replaceAll(' ', '') === '') {
            answer += 1;
        }
    }
    return answer;
}