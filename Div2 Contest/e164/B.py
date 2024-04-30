S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    n = int(input())
    a = L()
    a.append("END")
    cnt = 0
    cntl = []
    for i in a:
        if i == a[0]:
            cnt += 1
        else:
            cntl.append(cnt)
            cnt = 0
    if n == min(cntl):
        print(-1)
    else:
        print(min(cntl))
        



        
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()