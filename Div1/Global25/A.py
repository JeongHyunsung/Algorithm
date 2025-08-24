S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    n = int(input())
    l = input()
    s = 0
    for i in l:
        s += int(i)
    if n == 1 and s == 1:
        print("NO")
    elif n == 2 and s != 0:
        print("NO")
    elif s % 2 == 1:
        print("NO")
    elif s == 2 and "11" in l:
        print("NO")
    else:
        print("YES")
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()