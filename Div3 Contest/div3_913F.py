S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    n = int(input())
    l = L()
    l.extend(l)
    l1 = l.copy()
    l.reverse()
    l2 = l.copy()
    incs, decs = 0, 0
    incst, decst = 2*n-1, 2*n-1
    ans1, ans2 = -1, -1
    for i in range(2*n-2, -1, -1):
        if l1[i] < l1[i+1]:
            incs = 0
            decs += 1
            incst = i
        elif l1[i] > l1[i+1]:
            incs += 1
            decs = 0
            decst = i
        else:
            incs += 1
            decs += 1
        if decs == n-1:
            ans1 = 2*n-1-decst
            break
        if incs == n-1:
            ans1 = 2*n-incst
            break
    
    incs, decs = 0, 0
    incst, decst = 2*n-1, 2*n-1
    for i in range(2*n-2, -1, -1):
        if l2[i] < l2[i+1]:
            incs = 0
            decs += 1
            incst = i
        elif l2[i] > l2[i+1]:
            incs += 1
            decs = 0
            decst = i
        else:
            incs += 1
            decs += 1
        if decs == n-1:
            ans2 = 2*n-decst
            break
        if incs == n-1:
            ans2 = 2*n+1-incst
            break
    if n == 1:
        print(0)
    else:
        print(min(ans1, ans2))
    return

if __name__ == "__main__":
    for test in range(int(input())):
        solve()
