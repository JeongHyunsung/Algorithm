S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    n, m = S()
    a = L()
    cur = max(a)
    ans = []
    for i in range(m):
        c, l, r = input().split()
        l, r = int(l), int(r)
        if l <= cur <= r:
            if c == "+":
                cur += 1
            else:
                cur -= 1
        ans.append(cur)
    print(*ans)

    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()