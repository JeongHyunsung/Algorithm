S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    n, k = S()
    if k >= n-1:
        print(1)
    else:
        print(n)

    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()

