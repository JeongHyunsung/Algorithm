S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    n = int(input())
    l = L()
    ans = 0
    dt = {}
    for i in l:
        if i not in dt.keys():
            dt[i] = 1
        else:
            dt[i] += 1
    dt_s = []
    for key, value in sorted(dt.items()):
        dt_s.append(value)
    dt_sum = []
    sm = 0
    for i in dt_s:
        sm += i
        dt_sum.append(sm)
    for i in range(len(dt_s)):
        x = dt_s[i]
        if x >= 3:
            ans += (x * (x-1) * (x-2) / 6)
        if x >= 2 and i >= 1:
            ans += (x * (x-1) / 2) * dt_sum[i-1]
    print(int(ans))

    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()
