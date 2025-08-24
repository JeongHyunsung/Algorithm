S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    n = int(input())
    l = L()
    pos = [-1] * (n+1)
    ans = [0] * n
    for i in range(n):
        pos[l[i]] = i
    odd = 0
    if pos[n] % 2 == 1:
        odd = 1
    
    ev_num = n//2
    od_num = n//2
    if odd == 1:
        od_num = n
    else:
        ev_num = n

    for idx, i in enumerate(pos[1:]):
        if i % 2 == 1:
            ans[i] = od_num
            od_num -= 1
        else:
            ans[i] = ev_num
            ev_num -= 1
    print(*ans)
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()