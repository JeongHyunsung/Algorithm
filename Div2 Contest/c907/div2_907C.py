S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    an = [0, 1, 2, 3, 3, 4, 4]
    n = int(input())
    l = L()
    l.sort()
    top, tail = 0, n-1
    cnt = 0
    cur = -1
    ctl = -1
    if n == 1:
        if l[0] < 5:
            print(an[l[0]])
        else:
            print(1 + (l[0]+1)//2)
        return
    while top < tail:
        if cur == -1:
            cur = l[tail]
        if cur != 0:
            if cur >= l[top]:
                cur -= l[top]
                cnt += l[top]
                l[top] = 0
                top += 1
                ctl = 1
            else:
                cnt += cur
                l[top] -= cur
                cur = 0

        else:
            cnt += 1
            l[tail] = 0
            tail -= 1
            cur = l[tail]
            ctl = 0
    if cur == 0 and ctl == 1:
        cnt += 1
    elif ctl == 1 and cur != 0:
        cnt += 1 + (cur+1)//2
    else:
        
        if cur <= 5:
            cnt += an[cur]
        else:
            cnt += 1 + (cur+1)//2
    print(cnt)
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()
