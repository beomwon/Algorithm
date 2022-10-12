#include <iostream>
#include <string>
#define NMAX 100010
#define MOD 20150523
#define lint long long int
using namespace std;
 
string A, B;
 
lint num369[NMAX][10], tot369[NMAX];
lint mul3[NMAX][10][3], tot3[NMAX][3];
 
lint cntA, cntB;
 
// 거듭제곱
lint pow(lint val, int k) {
    if(k == 0) return 1;
    else if(k == 1) return val;
    else {
        if(k%2 == 0) return pow(( val*val )%MOD, k/2);
        else return ( val*pow(val*val%MOD, k/2) )%MOD;
    }
}
 
// 박수 횟수 구하기
lint get(string num) {
    lint ret, len;
 
    ret = 0;
    len = num.length();
 
    // 3, 6, 9가 포함된 숫자 카운트
    // Ex. 4237 >> (0000~3999) + (4000~4199) + (4200~4229) + (4230~4237)
    for(int idx=0, l=len;idx<len;idx++, l--) {
 
        // 예시: 4237
        // 현재 자릿수 이전 자릿수까지 박수 카운트 >> 000~999
        if(num[idx] > '0') ret = (ret + tot369[l-1]%MOD);
 
        // 현재 최대 자릿수 이전까지 박수 카운트 >> (1000~1999) + (2000~2999)
        int t = num[idx]-'0';
        for(int j=1;j<t;j++) ret = (ret + num369[l][j])%MOD;
 
 
        // 3, 6, 9가 포함된 경우, 남은 숫자 모조리 더하기
        if(num[idx] == '3' or num[idx] == '6' or num[idx] == '9') {
            // Ex. 3297에서 3000 카운트하기
            ret++;
 
            // 뒤에 있는 모든 숫자 더해서 결괏값에 반영
            lint t=0;
            for(int nxt =idx+1;nxt<len;nxt++) t = (t*10 + (num[nxt]-'0'))%MOD;
 
            ret = (ret + t)%MOD;
 
            // 탐색 종료
            break;
        }
    }
 
 
    // 3, 6, 9가 포함되지 않은 3의 배수 카운트
    int before=0;
    for(int idx=0, l=len;idx<len;idx++, l--) {
        // before: 이전까지 나온 숫자들의 합
        // m: 3의 배수를 만족하기 위해 필요한 값. Ex) before가 1일 때, m은 2
        int m = (3-before)%3;
 
        // 현재 자릿수 숫자가 0인 경우 스킵
        if(num[idx] == '0') {
            // 대신, 3의 배수이면서 10의 배수인 경우 카운트 Ex) 4200인 경우, 1 카운트
            if(m == 0 and idx+1 == len) ret++;
            else continue;
        }
 
        else {
            // 예시: 4237
            // 현재 숫자 이전 자릿수까지 카운트 >> 000~999
            ret = (ret + tot3[l-1][m])%MOD;
 
            // 현재 숫자 이전까지 카운트(단, 마지막 자리인 경우 끝까지 탐색)
            // Ex. 4237에서 현재 2인 경우) 4000~4199까지 탐색
            //     4237에서 현재 7인 경우) 0~7까지 모두 탐색
            int t = num[idx]-'0';
            if(idx+1 == len) t++;
 
            for(int j=1;j<t;j++) ret = (ret + mul3[l][j][m])%MOD;
 
            // 다음 탐색을 위한 갱신 및 점검
            before = (before+t)%3;
 
            // 현재 숫자가 3, 6, 9라면 조건(3, 6, 9를 포함하지 않는 3의 배수)를 만족하지 않기에 탐색 종료
            if(num[idx] == '3' or num[idx] == '6' or num[idx] == '9') break;
        }
    }
 
    return ret;
}
 
int check(string num) {
    // A가 박수쳐야 하는지 확인
    int f, tmp;
 
    f = tmp = 0;
    for(int i=0;i<num.length();i++) {
        if(num[i]=='3' or num[i]=='6' or num[i]=='9') {
            f = 1;
            break;
        }
        else tmp += (num[i]-'0');
    }
 
    if(f or tmp%3==0) return 1;
    else return 0;
}
 
int main() {
    // init
    ios::sync_with_stdio(false);
    cin.tie(0);
 
    // input
    cin >> A >> B;
 
    // 3, 6, 9가 포함된 숫자 구하기
    // num369[idx][j]: 자릿수가 idx이며, 맨 앞자리 숫자가 j일 때 박수치는 총 횟수
    tot369[1] = 3;
    num369[1][3] = num369[1][6] = num369[1][9] = 1;
    for(int idx=2;idx<=B.length();idx++) {
        for(int j= 0;j<=9;j++) {
            if(j>0 and j%3 == 0) num369[idx][j] = pow(10, idx-1);
            else num369[idx][j] = tot369[idx-1];
 
            tot369[idx] = (tot369[idx] + num369[idx][j])%MOD;
        }
    }
 
    // 3, 6, 9가 포함되지 않은 3의 배수 구하기
    // mul3[idx][j][k]: 자릿수가 idx이며, 맨 앞자리 숫자가 j이고, 3으로 나눴을 때 나머지가 k인 숫자의 개수
    tot3[0][0] = 1;
    for(int idx=1;idx<=B.length();idx++) {
        if(idx == 1) {
            for(int j=0;j<=9;j++) {
                if(j>0 and j%3 == 0) continue;
                else {
                    mul3[idx][j][j%3]++;
                    tot3[idx][j%3]++;
                }
            }
        }
 
        else {
            // 초깃값
            for(int k=0;k<3;k++) tot3[idx][k] = 0;
 
            for(int j=0;j<=9;j++) {
                // 3, 6, 9 제외
                if(j>0 and j%3 == 0) continue;
 
                for(int k=0;k< 3;k++) {
                    mul3[idx][j][k] = tot3[idx-1][(k-j + 12)%3];
 
                    tot3[idx][k] = (tot3[idx][k] + mul3[idx][j][k])%MOD;
                }
 
            }
        }
    }
 
    // A와 B까지 박수의 총합 구하기
    // check(num): num 숫자 확인하기
    // cntA: 0 ~ (A-1)까지 총 박수 횟수 / cntB: 1 ~ B까지 총 박수 횟수
    cntA = (get(A) - check(A) + MOD)%MOD;
    cntB = (get(B) + MOD)%MOD;
 
 
    cout << (cntB-cntA+MOD)%MOD;
 
}
 
/*
300 400
ans: 100
 
399 400
ans: 1
*/
