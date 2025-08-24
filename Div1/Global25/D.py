S = lambda: map(int, input().split())
L = lambda: list(S())


def rec(n, m):
    if n % 2 == 0 and n >= 2 * m:
        return n-m+1
    elif n % 2 == 1 and n >= 2 * m - 1:
        return n-m+1
    elif n == m:
        return 1
    elif n < m:
        return -1
    else:
        return -1


def solve():
    n, m = S()
    x = rec(n, m)
    if x == -1:
        print("NO")
    else:
        print("YES")
        print(5)
        print(x, 1, 1, 1, 1)
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()