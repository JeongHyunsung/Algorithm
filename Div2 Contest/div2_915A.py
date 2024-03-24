S = lambda: map(int, input().split())
L = lambda: list(S())

def solve():
    x, y = S()
    print(max(x, y))
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()

