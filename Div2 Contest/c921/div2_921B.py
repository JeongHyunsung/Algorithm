S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    x, n = S()
    dl = []
    for i in range(1, int(x**0.5+1)):
        if x % i == 0:
            dl.append(i)
    dl_n = len(dl)
    for i in range(dl_n-1, -1, -1):
        dl.append(x//dl[i])
    for i in dl:
        if i >= n:
            print(x//i)
            break
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()
        