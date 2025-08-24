S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    a, b, c = S()
    if (a + b + c) % 2 == 0:
        if (a+b) >= c:
            print((a+b+c)//2)
        else:
            print(a+b)
    else:
        print(-1)
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()