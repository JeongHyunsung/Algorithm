S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    n, q = S()
    a = L()
    x = L()
    pl = [0] * 30
    x_dec = [x[0]]
    cur = x[0]
    for i in x[1:]:
        if i < cur:
            x_dec.append(i)
            cur = i
    for i in x_dec:
        for j in range(i-1, 30):
            pl[j] += 2 ** (i-1)
    i_max = []
    for i in a:
        ad = -1
        for j in range(31):
            if i % 2**(j+1) != 0:
                ad = j
                break
        i_max.append(ad)
    ans_lst = []
    for idx, i in enumerate(a):
        if i_max[idx] != 0:
            ans_lst.append(i + pl[i_max[idx]-1])
        else:
            ans_lst.append(i)
        
    print(*ans_lst)
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()
