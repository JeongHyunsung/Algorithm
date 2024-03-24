S = lambda: map(int, input().split())
L = lambda: list(S())

def solve():
    n = int(input())
    s = input()
    ctl = 1
    for i in s:
        if i == "0":
            ctl = 0
            break
    if ctl:
        print("NO")
    else:
        print("YES")
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()

