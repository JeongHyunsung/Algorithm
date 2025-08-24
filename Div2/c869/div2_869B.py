S = lambda: map(int, input().split())
L = lambda: list(S())

def solve():
    n = int(input())
    if n == 1:
        print(1)
    elif n % 2 == 1:
        print(-1)
    else:
        ans = []
        for i in range(n//2, 0, -1):
            ans.append(i*2-1)
            ans.append(i*2)
        print(*ans)

    return

if __name__ == "__main__":
    for test in range(int(input())):
        solve()
