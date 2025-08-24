S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    x, y, k = S()
    
    if k % 2 == 1:
        print(x, y)
    for i in range(1, k//2+1):
        print(x-i, y)
        print(x+i, y)
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()