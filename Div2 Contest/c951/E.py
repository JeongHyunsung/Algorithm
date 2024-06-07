S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    n, d = S()
    dots = []
    for i in range(n):
        x, y = S()
        dots.append([x, y])
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()