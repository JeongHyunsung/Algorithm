S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    n = int(input())
    ans = []
    for i in range(1, n+1):
        ans.append(i*2)
    print(*ans)

    
if __name__ == "__main__":
    for test in range(int(input())):
        solve()
