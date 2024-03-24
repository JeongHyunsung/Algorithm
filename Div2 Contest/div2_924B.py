S = lambda: map(int, input().split())
L = lambda: list(S())

def solve():
    n = int(input())
    m = n-1 
    l = L()
    l = list(set(l))
    l.sort()
    crit = list(map(lambda x: x+m, l))

    cur = 0
    cur_crit = 0
    ob_list = []
    while cur < len(l):
        if l[cur] > crit[cur_crit]:
            cur_crit += 1
        else:
            cur += 1
            ob_list.append(cur_crit)
    ans_list = []
    for idx, i in enumerate(ob_list):
        ans_list.append(idx+1-i)
    print(max(ans_list))

    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()
