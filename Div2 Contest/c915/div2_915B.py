S = lambda: map(int, input().split())
L = lambda: list(S())

def solve():
    n = int(input())
    gh = [[] for i in range(n)]
    ans = 0
    for edge in range(n-1):
        u, v = S()
        u -= 1
        v -= 1
        gh[u].append(v)
        gh[v].append(u)
    for i in gh:
        if len(i) == 1:
            ans += 1
    print((ans+1)//2)

    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()

