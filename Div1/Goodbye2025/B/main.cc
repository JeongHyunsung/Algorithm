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
    string s;
    cin >> s;
    int cur = 0;
    int ans = 0;
    bool flag = false;

    while (cur < (int)s.size()){
        if(cur == 0 || cur == (int)s.size() - 1){
            if(s[cur] == 'u') ans += 1;
            flag = false;
        }
        else{
            if(s[cur] == 'u' && !flag){
                flag = true;
            }
            else if(s[cur] == 'u' && flag){
                ans += 1;
                flag = false;
            }
            else{
                flag = false;
            }
        }
        cur ++;
    }
    cout << ans << nl;

    // if there is "uu", it is always not suspicious


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