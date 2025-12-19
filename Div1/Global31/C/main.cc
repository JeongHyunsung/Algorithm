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
    ll n, k;
    cin >> n >> k;
    vector<ll> a(k);

    vector<bitset<64>> bits(k);
    bitset<64> n_2bit(n);

    bool flag = 0;
    int cur = 0;
    bool max_opt = 0;

    if(k % 2 == 1){
        for(int j=0; j<k; j++){
            a[j] = n;
        }
        cout << a << nl;
        return;
    }
    
    for(int i=63; i>=0; i--){
        if(!n_2bit[i] && !flag){
            continue;
        }

        if(n_2bit[i]){
            flag = true;
            for(int j=0; j<k; j++){
                if(j != cur) bits[j][i] = 1;
            }
            if(cur <= k-2){
                cur += 1;
            }
            else{
                max_opt = true;
            }
        }
        else{
            if(max_opt){
                for(int j=0; j<k; j++){
                    bits[j][i] = 1;
                }
                continue;
            }
            for(int j=0; j<cur-cur%2; j++){
                bits[j][i] = 1;
            }
        }
    }

    for(int j=0; j<k; j++){
        a[j] = bits[j].to_ullong();
    }
    cout << a << nl;
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