S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    n = int(input())
    l = L()
    l.sort()
    a, b, c, d = l[0], l[1], l[-1], l[-2];
    print(abs(a-c)+abs(c-b)+abs(b-d)+abs(d-a))
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()
