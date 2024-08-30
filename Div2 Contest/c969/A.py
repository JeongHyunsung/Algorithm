S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    l, r = S()
    odd = (r+1)//2 - (l)//2
    print(odd//2)


    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()