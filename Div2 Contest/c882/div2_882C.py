def solve():
    n = int(input())
    l = list(map(int, input().split()))
    cur = 0
    col = [0]
    for i in l:
        cur ^= i
        col.append(cur)
    col = set(col)
    m = -1
    for i in col:
        for j in col:
            can = i ^ j
            if can > m:
                m = can
    print(m)
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()