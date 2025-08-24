S = lambda: map(int, input().split())
L = lambda: list(S())

def solve():
    n, p, l, t = S()
    task_num = (n-1)//7 + 1
    wd = 0
    if (task_num//2 * (l+2*t)) >= p:
        wd = (p-1)//(l+2*t) + 1
    else:
        p -= (task_num//2 * (l+2*t))
        wd += task_num//2
        if task_num % 2 == 1:
            wd += 1
            p -= (l+t)
        if p > 0:
            wd += ((p-1)//l + 1)
    print(n-wd)
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()

