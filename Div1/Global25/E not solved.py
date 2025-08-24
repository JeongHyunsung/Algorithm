S = lambda: map(int, input().split())
L = lambda: list(S())

def rec(x, lst):
    ln = len(x) // 2 - 1
    ispd = True
    for i in range(ln):
        if x[i] != x[len(x)-1-i]:
            ispd = False
    if len(x) == 1:
        return False
    elif not ispd:
        lst.append(x)
        return True
    else:
        return rec(x[:ln+1], lst) and rec(x[ln+1:], lst)
        



def solve():
    st = input()
    ans_list = []
    ans = rec(st, ans_list)
    
    if not ans:
        print("NO")
    else:
        print("YES")
        print(len(ans_list))
        print(*ans_list)

    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()