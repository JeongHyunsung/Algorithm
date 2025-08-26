/// Created by nyaaaaa
#pragma GCC optimize("Ofast,unroll-loops,fast-math,inline,no-stack-protector")
//#pragma GCC target("avx2,avx,fma,bmi,bmi2,popcnt,lzcnt,tune=native")
#include <bits/allocator.h>
#include <bits/stdc++.h>
#define Task "task"
#define Nyaa main
#define fi first
#define se second
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define bit(i, x) (((x) >> (i)) & 1)
#define sz(x) (int)(x).size()
#define ntest int t; cin >> t; while (t--) solve()
#define __lcm(a, b) (1ll * ((a) / __gcd((a), (b))) * (b))
#define yes cout << "yes\n"
#define no cout << "no\n"
#define int ll
using namespace std;
typedef long long ll;
typedef long double db;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<pii> vii;
typedef vector<pll> vll;
mt19937_64 rng(chrono::steady_clock::now().time_since_epoch().count());
template <class X, class Y>
bool cmax(X &x, const Y &y) {
    return x < y ? x = y, true : false;
}
template <class X, class Y>
bool cmin(X &x, const Y &y) {
    return x > y ? x = y, true : false;
}
void solve() {
    int n; cin >> n; vi a(n);
    for (int &x : a) cin >> x;
    int sum = accumulate(all(a), 0ll), x = 0, y = 0;
    for (int i = 1; i < n; i++)
        tie(x, y) = make_pair(y, max(y, x + max(0ll, min(i, a[i]) - 2)));
    cout << sum - n + 1 - y << '\n';
}
Nyaa() {
    cin.tie(nullptr)->sync_with_stdio(false);
    if (fopen(Task".inp", "r")) {
        freopen(Task".inp", "r", stdin);
        //freopen(Task".out", "w", stdout);
    }
    ntest;
    cerr << "\nTime elapsed: " << 1000.0 * clock() / CLOCKS_PER_SEC << " ms.\n";
    return 0;
}