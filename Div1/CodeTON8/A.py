S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    n, k = S()
    ans = []
    if n == k:
        ans = [1] * n
        print(*ans)
    elif k == 1:
        ans = [i for i in range(1, n+1)]
        print(*ans)
    else:
        print(-1)
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()