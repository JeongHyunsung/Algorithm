import sys
S = lambda: map(int, input().split())
L = lambda: map(list(S()))

def solve():
    n, m = S()
    n_b, m_b = bin(n)[2:], bin(m)[2:]
    if len(n_b) == len(m_b):
        print(1)
        print(n, m)
        return
    n_del = 0
    one_cnt = 0
    for i in n_b:
        if i == "1":
            one_cnt += 1
        if one_cnt == 2:
            break
        n_del += 1
    n_b_del = n_b[n_del:]
    aft_1_op = 0
    if n_b_del != "":
        aft_1_op = 2 ** (len(n_b_del))-1

    if aft_1_op < m:
        print(-1)
    elif aft_1_op == m:
        print(1)
        print(n, m)
    else:
        print(2)
        print(n, aft_1_op, m)
    
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()
