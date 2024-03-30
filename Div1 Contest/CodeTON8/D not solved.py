S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    n, k = S()
    a = [[0]*n for _ in range(n)]
    for i in range(n):
        for idx, j in enumerate(L()):
            a[i][i+idx] = j
    print(a)

    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()