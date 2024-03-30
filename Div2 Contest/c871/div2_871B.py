def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.append(int(1))
    max = 0
    cnt = 0
    for i in range(n+1):
        if a[i] == 0:
            cnt += 1
        else:
            if max < cnt:
                max = cnt
            cnt = 0
    print(max)
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()
        