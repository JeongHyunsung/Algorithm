// cp_all_ds_lab_detailed.cpp
// GNU++17. Comprehensive DS + I/O + algorithms LAB with asserts and complexity notes.
//
// -------------------- Header map (what lives where) --------------------
// <iostream>           : cin/cout, I/O primitives
// <string>, <string_view> : std::string, std::string_view
// <vector>, <array>, <deque>, <list>, <forward_list>
// <stack>, <queue>     : stack/queue/priority_queue
// <set>, <map>, <unordered_set>, <unordered_map>
// <bitset>, <utility>(pair), <tuple>(tuple)
// <algorithm>          : sort/stable_sort, lower/upper/binary_search, unique, reverse,
//                         rotate, nth_element, partition, next_permutation, heap algos
// <numeric>            : accumulate, partial_sum, iota, gcd, lcm
// <sstream>            : istringstream for mock I/O
// <cmath>              : math
//
// For convenience in CP, people often do <bits/stdc++.h>, but below we
// explicitly list standard headers so you see where things come from.

#include <iostream>
#include <string>
#include <string_view>
#include <vector>
#include <array>
#include <deque>
#include <list>
#include <forward_list>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <bitset>
#include <utility>
#include <tuple>
#include <algorithm>
#include <numeric>
#include <sstream>
#include <cmath>
#include <cassert>

using namespace std;

using ll = long long;
#define all(x) begin(x), end(x)

template<class Range>
void print_seq(const Range& a, const string& sep=" ") {
    bool first = true;
    for (auto&& v : a) { if (!first) cout << sep; cout << v; first = false; }
    cout << '\n';
}

void section(const string& title) {
    cout << "\n================ " << title << " ================\n";
}

/*** 0) I/O PATTERNS (fast I/O, list, grid, line-split, EOF loop) ***/
void demo_io_patterns() {
    section("I/O Patterns");

    // In real contest code, always do:
    ios::sync_with_stdio(false);  // decouple iostream from stdio
    cin.tie(nullptr);             // no auto-flush on reads

    // We'll use a mock input so this file runs without external input.
    istringstream in(
        // single & multiple integers
        "5\n"
        "10 20 30 40 50\n"
        // grid h w + h lines (no spaces inside each row)
        "3 4\n"
        "abcd\n"
        "EFGH\n"
        "wxyz\n"
        // a full line with spaces
        "Hello world from CF\n"
        // EOF sequence of ints
        "7 8 9\n"
    );

    // 1) Single & list of ints: O(1) per token
    int n; in >> n;
    vector<int> a(n); for (auto& x : a) in >> x;
    assert(n == 5 && a.front()==10 && a.back()==50);

    // 2) Grid of characters (h x w), each row token: O(h*w)
    int h, w; in >> h >> w;
    vector<string> g(h);
    for (auto& row : g) in >> row;
    assert(h==3 && w==4 && g[1]=="EFGH");

    // 3) Read a whole line (with spaces): getline
    string dummy; getline(in, dummy); // consume leftover newline
    string line; getline(in, line);
    istringstream iss(line); // split by whitespace
    vector<string> tok; for (string s; iss >> s; ) tok.push_back(s);
    assert(tok.size()==4 && tok[2]=="from");

    // 4) Read until EOF: while (in >> x) ...
    vector<int> tail;
    for (int x; (in >> x); ) tail.push_back(x);
    assert((tail.size()==3) && tail[0]==7 && tail[1]==8 && tail[2]==9);

    cout << "I/O patterns OK\n";
}

/*** 1) PRIMITIVES & C-STYLE ARRAYS (built into the language; no headers needed) ***/
void demo_primitives_arrays() {
    section("Primitives & C-style Arrays");

    // Primitives: O(1) read/write
    int i = 42; long long L = 9000000000000000000LL; char c='X'; double d=3.14159;
    assert(i == 42 && c == 'X' && (long long)L/1000000000000000000LL == 9);

    // Static array: compile-time size, contiguous memory
    const int N = 6;
    int s[N] = {1,2,3};   // rest zero-initialized
    assert(s[0]==1 && s[5]==0);  // access O(1)

    // Dynamic array: new[]/delete[] on the heap (contiguous)
    int n = 5;
    int* dyn = new int[n];
    for (int k=0; k<n; ++k) dyn[k]=k*k;
    assert(dyn[4]==16);
    delete[] dyn;

    // 2D as a single flat block (contiguous, cache-friendly)
    int R=2, C=3;
    vector<int> A(R*C);
    auto at = [&](int r,int c)->int&{ return A[r*C + c]; };
    int t=1; for(int r=0;r<R;++r) for(int c=0;c<C;++c) at(r,c)=t++;
    assert(A.size()==6 && at(1,2)==6);

    cout << "Primitives & arrays OK\n";
}

/*** 2) STRING / STRING_VIEW (dynamic char array) ***/
void demo_string() {
    section("std::string / std::string_view");

    string s = "Hello, World!";
    // size()/length(): O(1) — number of chars
    assert(s.size()==13 && s.length()==13);

    // operator[]: O(1) direct access (no bounds check)
    assert(s[7]=='W');

    // at(i): O(1) with bounds checking (throws on out of range)
    assert(s.at(0)=='H');

    // front()/back(): O(1)
    assert(s.front()=='H' && s.back()=='!');

    // substr(pos,len): O(len) — allocates & copies those chars
    assert(s.substr(0,5)=="Hello");

    // find(pattern): average O(n*m) — naive search (n=len(s), m=len(pattern))
    assert(s.find("World")==7);
    // rfind(char/pattern): from the end, O(n*m)
    assert(s.rfind("o")==8);

    // find_first_of(set)/find_last_of(set): O(n*m) over char set
    assert(s.find_first_of("aeiou") == 1); // 'e' at idx 1
    assert(s.find_last_of ("aeiou") == 8); // last 'o' at idx 8

    // push_back(c): amortized O(1)
    s.push_back('a'); assert(s.back()=='a');

    // pop_back(): O(1)
    s.pop_back(); assert(s=="Hello, World!");

    // append/+=: O(k) — copies appended string of length k
    s += "abc"; assert(s=="Hello, World!abc");

    // insert(pos, sub): O(n+k) — shifts tail, inserts k chars
    s.insert(5, "_INS"); assert(s.substr(5,4)=="_INS");

    // erase(pos,len): O(n) — shifts tail left
    s.erase(5,4); assert(s=="Hello, World!abc");

    // replace(pos,len,sub): O(n+k) — remove len, insert sub
    s.replace(0,5,"Hi"); assert(s.find("Hi")==0);

    // clear(): O(1) logical clear (capacity stays)
    s.clear(); assert(s.empty());

    // assign(str): O(k) — replace content with k chars
    s.assign("ABCDE"); assert(s=="ABCDE");

    // resize(new_size, fill): O(k) — extend with fill or truncate
    s.resize(10,'x'); assert(s.size()==10 && s.back()=='x');

    // reserve(cap): amortized O(1) to O(n) — may reallocate bigger buffer
    size_t oldcap = s.capacity();
    s.reserve(64); assert(s.capacity() >= 64);

    // shrink_to_fit(): O(n) — non-binding request to reduce capacity
    s.shrink_to_fit(); (void)oldcap;

    // c_str()/data(): O(1) — pointer to internal char buffer (NUL-terminated for c_str)
    const char* p = s.c_str(); assert(p[0]=='A');

    // string_view: non-owning view, slicing is O(1) (no copy), lifetime must outlive view
    string_view sv = s;
    string_view head = sv.substr(0,3);
    assert(head=="ABC");

    cout << "string OK\n";
}

/*** 3) SEQUENTIAL CONTAINERS: vector / deque / list / forward_list ***/
void demo_sequential() {
    section("vector / deque / list / forward_list");

    // vector<T> — contiguous dynamic array
    //  - operator[] O(1), push_back/pop_back amortized O(1)
    //  - insert/erase in the middle O(n), size/capacity O(1)
    vector<int> v = {3,1,4,1,5};
    v.emplace_back(9);                          // amortized O(1)
    sort(all(v));                               // O(n log n)
    v.erase(unique(all(v)), v.end());           // unique O(n) + erase O(n)
    assert((v == vector<int>({1,3,4,5,9})));

    auto it = lower_bound(all(v), 4);           // O(log n) first >= 4
    assert(it != v.end() && *it == 4);
    assert(binary_search(all(v),5));            // O(log n)
    // capacity/reserve/shrink_to_fit demo
    size_t cap0 = v.capacity(); v.reserve(64);  // amortized O(1) (maybe O(n) if grow)
    v.shrink_to_fit(); (void)cap0;

    // deque<T> — segmented array, O(1) push/pop at both ends, O(1) random access
    deque<int> dq;
    dq.push_front(2); dq.push_back(3); dq.push_front(1); // [1,2,3]
    assert(dq.front()==1 && dq.back()==3 && dq[1]==2);
    dq.pop_front(); dq.pop_back();                       // [2]
    assert(dq.size()==1 && dq[0]==2);

    // list<T> — doubly-linked list (node-based)
    //  - insert/erase at known iterator O(1)
    //  - no random access; sort/unique provided
    list<int> L={3,1,4,1,5,9,2};
    L.sort();            // O(n log n)
    L.unique();          // O(n) on adjacent duplicates
    auto pos = next(L.begin(), 2);
    list<int> R={8,8};
    L.splice(pos, R);    // O(1) node transfer; R becomes empty
    assert(R.empty() && find(all(L),8)!=L.end());

    // forward_list<T> — singly-linked list
    //  - push_front O(1), insert_after/erase_after O(1), no size(), no random access
    forward_list<int> FL = {1,3,5};
    FL.push_front(0);                        // O(1) -> [0,1,3,5]
    auto fpos = FL.begin(); ++fpos;          // points to 1
    FL.insert_after(fpos, 2);                // [0,1,2,3,5]
    auto fpos2 = next(FL.begin(), 3);        // points to 3
    FL.erase_after(fpos2);                   // remove 5 -> [0,1,2,3]
    // Verify contents
    vector<int> flv; for (int x:FL) flv.push_back(x);
    assert((flv == vector<int>({0,1,2,3})));

    cout << "sequential OK\n";
}

/*** 4) ADAPTERS & HEAPS: stack / queue / priority_queue + heap algos ***/
void demo_adapters_heaps() {
    section("stack / queue / priority_queue + heap algorithms");

    // stack<T> — LIFO, O(1) push/pop/top
    stack<int> st; st.push(1); st.push(2); st.push(3);
    assert(st.top()==3); st.pop(); assert(st.top()==2);

    // queue<T> — FIFO, O(1) push/pop/front/back
    queue<int> q; q.push(1); q.push(2); q.push(3);
    assert(q.front()==1 && q.back()==3);
    q.pop(); assert(q.front()==2);

    // priority_queue<T> — binary heap
    //  - push/pop O(log n), top O(1), by default a max-heap
    priority_queue<int> maxh; for (int x : {5,1,9,3}) maxh.push(x);
    assert(maxh.top()==9); maxh.pop(); assert(maxh.top()==5);

    // Min-heap: use greater<T>
    priority_queue<int, vector<int>, greater<int>> minh;
    for (int x : {5,1,9,3}) minh.push(x);
    assert(minh.top()==1); minh.pop(); assert(minh.top()==3);

    // Heap algorithms directly on vector (need <algorithm>):
    // make_heap O(n), push_heap/pop_heap O(log n), sort_heap O(n log n)
    vector<int> h = {3,1,4,1,5,9};
    make_heap(all(h));               // now h.front() is max
    int before = h.front();
    h.push_back(6); push_heap(all(h));
    pop_heap(all(h)); int mx=h.back(); h.pop_back();
    sort_heap(all(h));               // h sorted ascending
    (void)before; (void)mx; // silence warnings
    assert(is_sorted(all(h)));

    cout << "adapters/heaps OK\n";
}

/*** 5) ORDERED/UNORDERED SETS & MAPS ***/
void demo_sets_maps() {
    section("set / multiset / unordered_set | map / unordered_map");

    // set<T> — ordered unique keys (red-black tree)
    //  insert/erase/find/lower_bound/upper_bound: O(log n)
    set<int> s = {5,1,9,3,3};
    assert(s.size()==4 && *s.begin()==1);
    auto lb = s.lower_bound(4); assert(lb!=s.end() && *lb==5);

    // multiset<T> — ordered, duplicates allowed
    multiset<int> ms = {1,1,2,2,3};
    auto it = ms.find(2);           // O(log n), points to one 2
    ms.erase(it);                   // erase by iterator: amortized O(1)
    assert(ms.count(2)==1);

    // unordered_set<T> — hash table; average O(1), worst O(n)
    unordered_set<int> us = {7,7,8,9};
    us.insert(10);
    assert(us.count(7)==1 && us.size()==4);
    // reserve to control rehashing (performance)
    us.reserve(32);
    double lf = us.load_factor(); (void)lf;

    // map<K,V> — ordered key->value (red-black tree), O(log n) ops
    map<string,int> mp;
    mp["alice"]=3; mp["bob"]=1; mp["carol"]=2;  // operator[] inserts default if missing
    assert(mp.begin()->first=="alice");
    auto mit = mp.lower_bound("b");             // first key >= "b"
    assert(mit->first=="bob");
    // try_emplace: O(log n), constructs value in-place if key missing
    mp.try_emplace("dave", 4); assert(mp["dave"]==4);

    // unordered_map<K,V> — hash table, average O(1) ops
    unordered_map<string,int> ump;
    ump.reserve(8);                     // reduce rehashing
    ump["xx"]=10; ump["yy"]=20; ump["zz"]=30;
    assert(ump.count("yy")==1 && ump.at("yy")==20);
    ump.erase("xx"); assert(!ump.count("xx"));
    ump.insert({"ASD", 104});


    cout << "sets/maps OK\n";
}

/*** 6) BITSET / PAIR / TUPLE / ARRAY<N> ***/
void demo_utilities() {
    section("bitset / pair / tuple / array<N>");

    // bitset<N> — fixed-size bit array; bit ops O(1) word-wise
    bitset<16> bs;                      // all zero
    bs.set(3);                          // set bit 3 -> O(1)
    bs.flip(3);                         // toggle -> back to 0
    bs.set(1).set(2);
    assert(bs.test(1) && bs.count()==2); // count O(N/word_size)
    bs.reset(2);                         // clear bit
    assert(bs.count()==1);
    // bit ops: &, |, ^, ~, <<, >> are supported
    bitset<16> bx; bx.set(1);
    auto by = bs | bx;                   // OR
    assert(by.count()>=1);

    // pair<T1,T2>
    pair<int,string> pr = {7,"hi"};
    assert(pr.first==7 && pr.second=="hi");

    // tuple<T...> with structured bindings
    tuple<int,string,double> tp = {1,"pi",3.14};
    auto [a,b,c] = tp;
    assert(a==1 && b=="pi" && fabs(c-3.14)<1e-12);

    // array<T,N> — fixed-size container with STL interface
    array<int,4> ar = {2,4,6,8};
    ar[2] = 7;             // O(1)
    ar.fill(1);            // O(N) assigns 1 to all
    assert(ar.size()==4 && ar[3]==1);

    cout << "bitset/pair/tuple/array OK\n";
}

/*** 7) <algorithm> & <numeric> CORE ROUTINES ***/
void demo_algo_numeric() {
    section("<algorithm> / <numeric> core");

    vector<int> v = {5,2,2,9,1,5,6};

    // sort: O(n log n) — not stable
    sort(all(v));
    assert(is_sorted(all(v)));

    // stable_sort: O(n log n), preserves equal-elements order
    struct P { int key; int id; };
    vector<P> vp = {{2,0},{2,1},{1,2},{1,3}};
    stable_sort(all(vp), [](const P& L, const P& R){ return L.key < R.key; });
    // after sort: ids within equal keys remain in original order
    assert(vp[0].key==1 && vp[0].id==2 && vp[1].id==3);

    // binary_search / lower_bound / upper_bound: O(log n) on sorted range
    bool has5 = binary_search(all(v), 5);
    auto L = lower_bound(all(v),5) - v.begin(); // first >= 5
    auto U = upper_bound(all(v),5) - v.begin(); // first > 5
    assert(has5 && (U-L)>=1);

    // unique + erase-idiom: O(n) + O(n) on average
    v.erase(unique(all(v)), v.end());
    assert((v == vector<int>({1,2,5,6,9})));

    // reverse: O(n)
    reverse(all(v)); assert(v.front()==9 && v.back()==1);

    // rotate: O(n) — put v[k] at front
    rotate(v.begin(), v.begin()+2, v.end()); // logical left shift by 2
    // verify size unchanged
    assert(v.size()==5);

    // nth_element: average O(n) — v[k] is the element as if sorted; left <= v[k], right >= v[k]
    vector<int> w = {9,8,7,6,5,4,3,2,1};
    nth_element(w.begin(), w.begin()+3, w.end());
    int kth = w[3];
    // all elements [0..3] <= kth, [3..end) >= kth
    assert(*max_element(w.begin(), w.begin()+4) <= kth);
    assert(*min_element(w.begin()+3, w.end())   >= kth);

    // partition: O(n) — reorders so that pred(x) true come first (order not preserved)
    vector<int> par = {1,2,3,4,5,6};
    auto mid = partition(all(par), [](int x){ return x%2==0; });
    // [begin, mid) are even
    assert(all_of(par.begin(), mid, [](int x){return x%2==0;}));

    // next_permutation: O(n) — lexicographic next; returns false when wraps
    vector<int> perm = {1,2,3};
    bool ok = next_permutation(all(perm)); // -> {1,3,2}
    assert(ok && perm[1]==3);

    // min_element / max_element: O(n)
    assert(*min_element(all(v)) <= *max_element(all(v)));

    // <numeric>: iota / accumulate / partial_sum / gcd / lcm
    vector<int> a(5); iota(all(a), 1);            // [1..5]
    int sum = accumulate(all(a), 0);              // O(n)
    assert(sum==15);
    vector<int> ps(5); partial_sum(all(a), ps.begin()); // O(n)
    assert((ps == vector<int>({1,3,6,10,15})));
#if __cplusplus >= 201703L
    // gcd/lcm are in <numeric> since C++17: O(log min(a,b))
    assert(gcd(24,36)==12 && lcm(24,36)==72);
#endif

    cout << "algorithms/numeric OK\n";
}

int main() {
    cout << "C++ Competitive Programming DS + I/O + Algorithms LAB\n";
    demo_io_patterns();
    demo_primitives_arrays();
    demo_string();
    demo_sequential();
    demo_adapters_heaps();
    demo_sets_maps();
    demo_utilities();
    demo_algo_numeric();
    cout << "\n[ALL TESTS PASSED]\n";
    return 0;
}
