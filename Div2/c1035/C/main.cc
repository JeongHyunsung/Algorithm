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
    ull n, l, r, k;
    cin >> n >> l >> r >> k;
    if(n%2 == 1){
        cout << l << nl;
        return;
    }
    //clear
    else if(n == 2){
        cout << -1 << nl;
        return;
    }
    //clear
    else{
        bitset<64> bs(l);
        int msb = -1;
        for(int i = 63; i>=0; i--){
            if(bs[i]){msb = i; break;}
        }
        ull x = 1ULL << (msb+1);

        if(x > r) cout << -1 << nl;
        else{
            if(k <= n-2) cout << l << nl;
            else cout << x << nl;
        }
    }
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