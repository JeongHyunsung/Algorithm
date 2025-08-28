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

void solve(){
    ull n, k;
    cin >> n >> k;
    string st;
    cin >> st;
    vector<ull> s;
    for(char &c : st){
        s.push_back(c - '0');
    }
    vector<ull> ans(n);

    ull cnt = 0;
    // consecutive 한 1 이 k 개 이상이면 -1,
    // 그렇지 않다면, 0에 높은수 다 + 1에 낮은수 다 
    
    for (auto v : s){
        if (v == 1) cnt ++ ;
        else cnt = 0;
        if (cnt >= k){
            cout << "NO" << nl;
            return;
        }
    }

    ull start, end;
    start = 1;
    end = n;

    for (ull i = 0; i<n; i++){
        if(s[i] == 0){
            ans[i] = end--;
        }
        else{
            ans[i] = start++;
        }
    }
    cout << "YES" << nl;
    cout << ans << nl;
    return;
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