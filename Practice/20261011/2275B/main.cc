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
    int n;
    cin >> n;
    string s;
    cin >> s;
    stack<int> st;
    vector<bool> printed(n, false);
    vector<int> ans;

    
    // if 3, it is printed. 
    // if 2, it is not printed if there is unprinted 1. 
    // if 1, it is printed if there is 2 before meeting 1.

    for(int i=0; i<n; i++){
        if(s[i] == '1'){
            st.push(i);
        }
        else if(s[i] == '2'){
            if (!st.empty()){
                printed[st.top()] = true;
                st.pop();
            }
            else{
                printed[i] = true;
            }
        }
        else{
            printed[i] = true;
        }
    }
    for(int i=0; i<n; i++){
        if(!printed[i]){
            ans.push_back(i+1);
        }
    }
    cout << ans.size() << nl;
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