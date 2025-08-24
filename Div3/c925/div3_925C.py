import sys
input = sys.stdin.readline
S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    n = int(input())
    l = L()
    if n == 1:
        print(0)
    else:
        a, b = l[0], l[-1]
        ac, bc = -1, -1
        for idx, i in enumerate(l):
            if i != a:
                ac = idx
                break
        for idx, i in enumerate(l[::-1]):
            if i != b:
                bc = idx
                break
        if ac == -1:
            print(0)
        elif a != b:
            print(n-max(ac, bc))
        else:
            print(n-ac-bc)
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()
