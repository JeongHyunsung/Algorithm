S = lambda: map(int, input().split())
L = lambda: list(S())

import math


def solve():
    n = int(input())
    g = [[] for _ in range(n)]
    leaf = []
    for i in range(n-1):
        u, v = map(lambda x: int(x)-1, input().split())
        g[u].append(v)
        g[v].append(u)
    s = input()
    for idx, i in enumerate(g):
        if len(i) == 1 and idx != 0:
            leaf.append(idx)

    modify_leaf = []
    zero_cnt = 0
    one_cnt = 0
    non_leaf_q = 0
    for i in leaf:
        if s[i] == "?":
            modify_leaf.append(i)
        elif s[i] == "1":
            one_cnt += 1
        else:
            zero_cnt += 1
    for i in range(n):
        if s[i] == "?" and i != 0:
            non_leaf_q += 1
    non_leaf_q -= len(modify_leaf)
    
    if s[0] == "?":
        if one_cnt > zero_cnt: 
            ans = one_cnt + len(modify_leaf)//2 
        elif zero_cnt > one_cnt:
            ans = zero_cnt + len(modify_leaf)//2
        else:
            if non_leaf_q % 2 == 1:
                ans = one_cnt + (len(modify_leaf)+1)//2
            else:
                ans = one_cnt + len(modify_leaf)//2
    else:
        if s[0] == "1":
            ans = zero_cnt + (len(modify_leaf)+1)//2
        else:
            ans = one_cnt + (len(modify_leaf)+1)//2
    print(ans)
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()