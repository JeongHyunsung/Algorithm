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
    ll n; 
    cin >> n;
    vector<ll> a(n);
    cin >> a;

    map<ll, pair<ll, vector<ll>>> cache; // counter + latest start
    vector<ll> dp(n);

    for (ll i = 0; i < n; i++) {
        cache[a[i]].second.push_back(i);
        cache[a[i]].first++;
        if(i==0) dp[i] = 0;
        else dp[i] = dp[i-1];
        if (cache[a[i]].first >= a[i]) {
            ll minima;
            if(i==0) minima = 0;
            else minima = dp[i-1];
            if(cache[a[i]].second[cache[a[i]].second.size() - a[i]]-1 < 0){
                dp[i] = max(minima, a[i]);
            }
            else{
                dp[i] = max(minima, dp[cache[a[i]].second[cache[a[i]].second.size() - a[i]]-1] + a[i]);
            }
            
        }
    }
    
    cout << dp.back() << nl;
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