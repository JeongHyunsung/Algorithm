S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    n = int(input())
    a = L()
    d = [False] * (n+1)
    mex = 0
    ans = []
    for idx in range(n):
        
        if a[idx] > 0:
            ans_x = mex
        else:
            ans_x = mex - a[idx]
        ans.append(ans_x)

        d[ans_x] = True
        if ans_x == mex:
            while d[mex]:
                mex += 1
    print(*ans)
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()