S = lambda: map(int, input().split())
L = lambda: list(S())

import math


def solve():
    n, a, b = S()
    c = L()
    gcd = math.gcd(a, b)
    if n == 1:
        print(0)
        return
    
    if gcd == 0:
        d = c[:]
    else:
        d=list(map(lambda x: x%gcd, c))
    cur_ans = max(d) - min(d)
    d.sort()
    for i in range(n-1):
        cur_ans = min(cur_ans, d[i]+gcd-d[i+1])
    print(cur_ans)
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()