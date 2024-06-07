S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    n = int(input())
    l = L()
    num = 232792560
    ans = []
    for i in l:
        ans.append(num//i)
    if sum(ans) < num:
        print(*ans)
    else:
        print(-1)

    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()