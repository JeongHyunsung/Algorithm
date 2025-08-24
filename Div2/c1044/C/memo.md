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


void query(const int n, const vector<int> &x){
    cout << "? " << n << " " << x.size() << " " << x << endl;
}

int scan(){
    int val;
    if (!(cin >> val)) exit(0);
    return val;
}

void answer(const vector<int> &x){
    cout << "! " << x.size() << " " << x << endl;
}

void solve(){
    int n;
    cin >> n;

    vector<int> b(n);
    iota(all(b), 1);

    vector<pair<int, int>> data(n);

    for (int i = 1; i < n+1; i++){
        query(i, b);
        int res = scan();
        data[i-1] = {i, res};
    }

    sort(data.begin(), data.end(), [](const pair<int,int>& x, const pair<int,int>& y){
        return x.second > y.second;
    });

    int cur = 1;
    int bl = -1;
    vector<int> ans;
    ans.push_back(data[0].first);
    
    while(true){
        if (cur == n) break;
        else if(bl == data[cur].second){
            cur ++;
            continue;
        }
        else{
            vector<int> b2 = b;
            b2.erase(b2.begin() + (data[cur].first - 1));
            query(ans[0], b2);
            int res = scan();
            if(res != data[0].second){
                ans.push_back(data[cur].first);
                bl = data[cur].second;
            }
            cur++;
        }
        
    }

    answer(ans);

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