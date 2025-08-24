S = lambda: map(int, input().split())
L = lambda: list(S())

def solve():
    n, b, x = S()
    c = L()
    c.sort()
    numd = [0] * 2e5+1

    for idx, i in enumerate(c):
        numd[i] += 1
        
    for i in range(1, 2e5+1):
        dec = (i-1) * x
        


    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()
