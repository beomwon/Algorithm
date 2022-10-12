#include <bits/stdc++.h>
using namespace std;

int c[111][111];
int f[111][111];
int bias = 50;
int n;
vector<int> g[111];
int par[111];

int a[55], b[55];
int asum, bsum;

int s = 101, t = 102;

void init(int x){
	memset(f, 0, sizeof f);
	for(int i=1; i<=n; i++){
		for(int j=1; j<=n; j++){
			c[i][j+bias] = x;
		}
	}
}

bool chk(int x){
	init(x);
	int res = 0;
	while(1){
		memset(par, -1, sizeof par);
		queue<int> q; q.push(s);
		while(q.size()){
			int now = q.front(); q.pop();
			for(auto nxt : g[now]){
				if(par[nxt] == -1 && c[now][nxt] - f[now][nxt] > 0){
					par[nxt] = now; q.push(nxt);
				}
			}
		}
		int flow = 1e9+7;
		if(par[t] == -1) break;
		for(int i=t; i!=s; i=par[i]){
			int a = par[i], b = i;
			flow = min(flow, c[a][b] - f[a][b]);
		}
		res += flow;
		for(int i=t; i!=s; i=par[i]){
			int a = par[i], b = i;
			f[a][b] += flow; f[b][a] -= flow;
		}
	}
	return asum == bsum && asum == res;
}

int main(){
	ios_base::sync_with_stdio(0); cin.tie(0);
	cin >> n;
	for(int i=1; i<=n; i++) cin >> a[i], asum += a[i];
	for(int i=1; i<=n; i++) cin >> b[i], bsum += b[i];
	for(int i=1; i<=n; i++){
		g[s].push_back(i);
		c[s][i] = a[i];
		c[i+bias][t] = b[i];
		g[i+bias].push_back(t);
	}
	for(int i=1; i<=n; i++){
		for(int j=1; j<=n; j++){
			g[i].push_back(j+bias);
			g[j+bias].push_back(i);
		}
	}

	int l = 0, r = 10000;
	int ans = -1;
	while(l <= r){
		int m = l + r >> 1;
		if(chk(m)){
			ans = m; r = m - 1;
		}else{
			l = m + 1;
		}
	}
	cout << ans << "\n";
	chk(ans);
	for(int i=1; i<=n; i++){
		for(int j=1; j<=n; j++){
			cout << f[i][j+bias] << " ";
		}
		cout << "\n";
	}
}