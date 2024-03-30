def solve():
    n = int(input())
    a, b = [], []
    for bk in range(n): 
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    min1, min2, min3 = 1e10, 1e10, 1e10
    for i in range(n):
        if b[i] == 1:
            if min1 > a[i]:
                min1 = a[i]
        if b[i] == 10:
            if min2 > a[i]:
                min2 = a[i]
        if b[i] == 11:
            if min3 > a[i]:
                min3 = a[i]
    if (min1 == 1e10 or min2 == 1e10) and min3 == 1e10:
        print(-1)
    else:
        print(min(min1+min2, min3))
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()
        