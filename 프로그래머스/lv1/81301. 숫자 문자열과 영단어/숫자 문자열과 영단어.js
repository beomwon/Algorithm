function solution(s) {
    n = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for (let i = 0; i < 10; i++) {
        
        s = s.replaceAll(n[i], i.toString())
    }
    return Number(s);
}