#include <bits/stdc++.h>
using namespace std; 

using ll = long long;
using ull = unsigned long long;
using ld = long double;

#define all(x) begin(x), end(x)
const char nl = '\n';
const int INF = 0x3f3f3f3f;
const ll INF64 = (1LL<<62);

template<class T>
ostream& operator<<(ostream& os, const vector<T>& v){
    for (int i=0; i<(int)v.size(); i++){
        if(i) os << ' ';
        os << v[i];
    }
    return os; 
}

template<class T>
istream& operator>>(istream& is, vector<T>& v){
    for (auto &x : v) is >> x;
    return is;
}

template<class T>
void print_matrix(const vector<vector<T>>& v){
    for (auto &row : v){
        for (int j=0; j<(int)row.size(); j++){
            if (j) cout << ' ';
            cout << row[j];
        }
        cout << nl;
    }
}

template<class T>
vector<vector<T>> read_matrix(int n, int m){
    vector<vector<T>> a(n, vector<T>(m));
    for (int i=0; i<n; i++) for (int j=0; j<m; j++) cin >> a[i][j];
    return a;
}



void dfs(int u, int p, const vector<vector<ull>>& graph, vector<bool>& visited, vector<bool>& in_cycle, vector<ull>& parent, vector<ull>& stack) {
    visited[u] = true;
    stack.push_back(u);
    for (ull v : graph[u]) {
        if (v == p) continue;
        if (!visited[v]) {
            parent[v] = u;
            dfs(v, u, graph, visited, in_cycle, parent, stack);
        } else if (find(stack.begin(), stack.end(), v) != stack.end()) {
            for (int i = stack.size() - 1; i >= 0; --i) {
                in_cycle[stack[i]] = true;
                if (stack[i] == v) break;
            }
        }
    }
    stack.pop_back();
}

void solve(){
    ull n, m, V;
    cin >> n >> m >> V;

    vector<ull> a(n);
    cin >> a;
    vector<vector<ull>> graph(n);
    for(ull i=0; i<m; i++){
        ull u, v;
        cin >> u >> v;
        graph[u-1].push_back(v-1);
        graph[v-1].push_back(u-1);
    }

    vector<bool> in_cycle(n, false);
    vector<bool> visited(n, false);
    vector<ull> parent(n, -1);
    vector<ull> stack;
    for (ull i = 0; i < n; i++) {
        if (!visited[i]) dfs(i, -1, graph, visited, in_cycle, parent, stack);
    }


    ull ans = 1;
    for(ull i=0; i<n; i++){
        if(a[i] != -1) continue;
        if(!in_cycle[i]){
            ans *= V;
            ans = ans % 998244353ULL;
        }
    }

    cout << ans << nl;

}

int main(){


    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int tests;
    cin >> tests;
    while(tests--){
        solve();
    }
    return 0;
}