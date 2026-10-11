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
    // |a| is the size of array, 
    // f(a) is the number of unique subarray of a, s.t. xor of all elememts in the subsrray is 0;
    // find maximmum |a|-f(a) for arbitary size of array a, s.t. all elements in a are in [0, n].

    // observation: if we add a single element to a array with size n-1, the number of uniqeu subarray increase with n. 
    // for example, if we have a = [0, 1] and add 2, [2], [1,2], [0,1,2] are new unique subarrays.

    // then, can we build it with a greedy approach?
    // we select one digit from [0, log2(n)], and then, next digit should avoid same digit, additionally, we should avoid the digit that is the xor of all previous digits.
    // if we greedily select this digit, this banned selection will be always different. However, we have only floor(log2(n)) + 1 digits, and n options, 

    // example n=2
    // 01 => 10 => (no 10, no 11) 01 => (no 01, no 11, no 10) 00 (+1) => (no 00, no 01, no 11, no 10) 01 **critical observation, after using all options, we need to add at least 1 into f(a).


    // example n=5 
    // 001 => 010 => 001 => 100 => (no 100, no 101, no 111, no 110) 001 => 

    // pattern : 1 => 121 => 1214121 => 
    // no 1, no 3, no 2, no 7, no 6, no 4, no 5 ====> 0 (no satisfied subarray end here. also, no strt here) => repeat! 
    int n;
    cin >> n;
    
    vector<int> a = {1};
    vector<int> a_dup;

    int a_digits = floor(log2(n)) + 1; // for example, 5 ==> 2 + 1 
    for (int i=1; i<a_digits; i++){
        a_dup = a;
        a.push_back(1 << i);
        a.insert(a.end(), a_dup.begin(), a_dup.end());
    }

    a_dup = a;
    a.push_back(0);
    a.insert(a.end(), a_dup.begin(), a_dup.end());
    cout << a.size() << endl;
    cout << a << endl;
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