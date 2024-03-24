S = lambda: map(int, input().split())
L = lambda: list(S())

def solve():
    n = int(input())
    min = 0
    max = 1e9+1
    nt = []
    for line in range(n):
        a, x = S()
        if a == 1 and x > min:
            min = x
        elif a == 2 and x < max:
            max = x
        else:
            nt.append(x)
    ans = max-min+1
    nt = set(nt)
    for i in nt:
        if min<=i<=max:
            ans -= 1
    if ans < 0:
        print(0)
    else:
        print(ans)
    
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()

