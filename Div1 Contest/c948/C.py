S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    n = int(input())
    l = L()
    l.sort()
    print(l[-2])
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()