def solve():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    or_res = 0
    cur = 0
    while cur <= n-1 and (x^(or_res|a[cur]))|x == x:
        or_res |= a[cur]
        cur += 1
    cur = 0
    while cur <= n-1 and (x^(or_res|b[cur]))|x == x:
        or_res |= b[cur]
        cur += 1
    cur = 0
    while cur <= n-1 and (x^(or_res|c[cur]))|x == x:
        or_res |= c[cur]
        cur += 1
    if or_res == x:
        print("Yes")
    else:
        print("No")
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()