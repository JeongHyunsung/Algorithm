S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    n = int(input())
    l = L()
    ans = 1
    for i in range(n-1):
        if i == 0 or i == 1 or i == 3 or i == 7 or i == 15:
            continue
        else:
            if l[i] > l[i+1]:
                ans = 0

    if ans:
        print("YES")
    else:
        print("NO")

    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()
