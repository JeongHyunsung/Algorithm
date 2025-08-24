S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    n, k = S()
    ans = ""
    for i in range(n):
        for j in range(k):
            ans += chr(ord("a")+j)
    print(ans)
    
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()
