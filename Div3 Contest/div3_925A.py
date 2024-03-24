import sys
input = sys.stdin.readline
S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    n = int(input())
    n -= 3
    #0 ~ 25
    a, b, c = 0, 0, 0
    if n >= 50:
        a = n-50
        b = 25
        c = 25
    elif n >= 25:
        a = 0
        b = n-25
        c = 25
    else:
        a, b, c = 0, 0, n
    a, b, c = chr(ord("a")+a),chr(ord("a")+b), chr(ord("a")+c)
    print(a+b+c)

    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()
