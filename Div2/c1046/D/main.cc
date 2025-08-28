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

void query(char&& c, ll&& x){
    cout << "? " << c << " " << x << endl;
}

ll scan(){
    ll val;
    if (!(cin >> val)) exit(0);
    return val;
}

void answer(const ll& x, const ll& y){
    cout << "! " << x << " " << y << endl;
}

void solve(){
    int n;
    cin >> n;

    vector<pair<ll, ll>> anch(n);
    for (int l = 0; l<n; l++){
        cin >> anch[l].first >> anch[l].second;
    }

    pair<ll, ll> LU;
    pair<ll, ll> RU;
    ll max_lu = -INF64;
    ll max_RU = -INF64;
    for (auto cord: anch){
        if (cord.first + cord.second > max_RU){
            RU = cord;
            max_RU = cord.first + cord.second;
        }
        if (cord.second - cord.first > max_lu){
            LU = cord;
            max_lu = cord.second - cord.first;
        }
    }

    // map anchor point 의 가장 왼쪽 위, 오른쪽 위로 가서 측정한다면, 어떤 anchor 에서 측정된 결과인지를 특정 가능
    // 원본의 좌표 또한 유추 가능.

    query('L', 1e9);
    scan();
    query('L', 1e9);
    scan();
    query('U', 1e9);
    scan();
    query('U', 1e9);
    ll ans1 = scan();
    query('R', 1e9);
    scan();
    query('R', 1e9);
    scan();
    query('R', 1e9);
    scan();
    query('R', 1e9);
    ll ans2 = scan();

    ll delta_x = RU.first - LU.first;

    ll exact_LU_y = (RU.second + LU.second + (ans2 + ans1 - (4e9 - delta_x))) / 2;
    
    ll exact_LU_x = LU.first - (ans1 - (exact_LU_y - LU.second));

    ll exact_x = exact_LU_x + 2e9;
    ll exact_y = exact_LU_y - 2e9;

    answer(exact_x, exact_y);

    

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