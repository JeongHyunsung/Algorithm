S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    n, k = S()
    l = L()
    ans = 10
    for i in l:
        c = k - i%k
        if c == k:
            c = 0
        if c < ans:
            ans = c
    if k == 4 and n >= 2:
        cnt = 0
        c = 10
        for i in l:
            if i % 2 == 0:
                cnt += 1
        if cnt == 0:
            c = 2
        elif cnt == 1:
            c = 1
        else:
            c = 0
        if c < ans:
            ans = c
    print(ans)
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()
