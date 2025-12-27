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
    int n, m;
    cin >> n >> m;

    vector<ll> a(n);
    cin >> a;

    vector<pair<ll, int>> v;
    for(int i=0; i<n; i++){
        v.push_back({a[i], i+1});
    }
    sort(v.begin(), v.end());
    sort(a.begin(), a.end());
    // attack is only one time per each elve
    // if one attack another, 1 or 2 elve will die 

    // 1. since attack is symmetric, we can terminate if n/2 elves attack.
    // 2. If m > n/2, it is impossible 
    // 3. tournament style

    if(2*m > n){
        cout << -1 << nl;
        return;
    }

    auto add_chain = [&](int start, int end, bool reversed=false){
        if(reversed){
            for(int i=start; i<end-1; i++){
                cout << v[i].second << ' ' << v[i+1].second << nl;
            }
        }
        else{
            for(int i=start; i<end-1; i++){
                cout << v[i+1].second << ' ' << v[i].second << nl;
            }
        }
    };

    if(m == 0){
        if(accumulate(all(a), 0LL) >= 2 * a[n-1]){
            int threshold;
            ll sum = 0;
            for(int i=n-2; i>=0; i--){
                sum += a[i];
                if(sum >= a[n-1]){
                    threshold = i;
                    break;
                }
            }
            cout << n-1 << nl;
            add_chain(0, threshold+1, true);
            for(int i=threshold; i<n-1; i++){
                cout << v[i].second << ' ' << v[n-1].second << nl;
            }

        }
        else{
            cout << -1 << nl;
        }
        return;
    }

    cout << n-m << nl;
    for(int i=0; i<m; i++){
        if(i!=m-1) add_chain(2*i, 2*i+2);
        else add_chain(2*i, n);
    }
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