S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    n = int(input())
    lst = L()
    pos = [-1] * n
    cg = [-1] * n
    for idx, i in enumerate(lst):
        pos[i-1] = idx
    for i in range(n):
        cg[i] = pos[i] - i
    ans = -1
    for i in cg:
        if i and ans == -1:
            ans = i
        elif i:
            a, b = abs(ans), abs(i)
            while True:
                if a>b:
                    a = a%b
                else:
                    b = b%a
                if a * b == 0:
                    ans = a + b
                    break
    print(ans)

    


    
if __name__ == "__main__":
    for test in range(int(input())):
        solve()
