S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    n = int(input())
    perm = L()
    ans = []

    for i in perm:
        if i < n:
            ans.append(i+1)
        else:
            ans.append(1)
    print(*ans)
    

    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()