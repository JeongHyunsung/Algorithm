S = lambda: map(int, input().split())
L = lambda: map(list(S()))

def solve():
    n = int(input())
    ans = 1
    for i in range(100):
        if n >= 2**i:
            ans = 2**i
    print(ans)

    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()
