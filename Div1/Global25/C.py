S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    n, m, k = S()
    a = L()
    a.sort()
    req = k // m
    if k % m != 0:
        req += 1
        fix = m * ((req-1) * (k%m) + ((req-1)*(req-2))//2 * m)
        print(fix + sum(a[0:req-1])*m + a[req-1]* (k%m) )
    else:
        fix = ((req-1)*(req))//2 * m * m
        print(fix + sum(a[0:req])*m)
    
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()