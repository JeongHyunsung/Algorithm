def solve():
    n = int(input())
    l = list(map(int, input().split()))
    opt = l[0]
    for i in l:
        opt &= i
    if opt:
        print(1)
        return
    else:
        cur, cnt = 0, 0
        cur_a = -1
        while cur <= n-1:
            if cur_a == -1:
                cur_a = l[cur]
            else:
                cur_a &= l[cur]
            if cur_a == 0:
                cnt += 1
                cur_a = -1
            cur += 1
        print(cnt)
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()