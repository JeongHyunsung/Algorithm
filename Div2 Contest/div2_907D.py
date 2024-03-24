S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    q = int(input())
    dt = []
    for i in range(2, 62):
        #range = 2** i ~ 2**(i+1)-1
        cnt = 0
        nm = 2 ** i
        while nm >= i:
            nm //= i
            cnt += 1
        dt.append([2**i, cnt])
        if i ** cnt < 2 ** (i+1)-1 < i ** (cnt+1):
            continue
        else:
            dt.append([i**(cnt+1), cnt+1])
    ans_lst = []

    for qer in range(q):
        a, b = S()
        ac, bc = 0, 0
        for i in range(len(dt)-1):
            if dt[i][0] <= a < dt[i+1][0]:
                ac = i
            if dt[i][0] <= b < dt[i+1][0]:
                bc = i
        sm = 0
        if ac == bc:
            ans_lst.append((dt[ac][1] * (b-a+1)) % (10**9 + 7))
        else:
            for i in range(ac+1, bc):
                sm += dt[i][1] * (dt[i+1][0]-dt[i][0])
            sm += dt[ac][1] * (dt[ac+1][0] - a)
            sm += dt[bc][1] * (b - dt[bc][0] + 1)
            ans_lst.append(sm % (10**9 + 7))
    for i in ans_lst:
        print(i)

    return


if __name__ == "__main__":
    solve()
