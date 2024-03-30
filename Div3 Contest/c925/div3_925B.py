import sys
input = sys.stdin.readline
S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    n = int(input())
    l = L()
    x = sum(l)//n
    m = 0
    flag = 1
    for i in l:
        m += i - x
        if m < 0:
            flag = 0
    if flag:
        print("YES")
    else:
        print("NO")
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()
