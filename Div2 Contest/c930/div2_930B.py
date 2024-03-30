S = lambda: map(int, input().split())
L = lambda: map(list(S()))

def solve():
    n = int(input())
    a = input()
    b = input()
    ans = 1
    ans_list = [a[0]]
    cur = 0
    state = 0
    while cur < n-1:
        op1, op2 = int(a[cur+1]), int(b[cur])
        cur += 1
        if op1 == op2 and state == 0:
            state = 1
            ans += 1
            ans_list.append(op1)
        elif op1 == op2 and state == 1:
            ans += 1
            ans_list.append(op1)
        elif op1 == 0 and state == 1:
            ans_list.append(0)
            ans = 1
            state = 0
        elif op2 == 0 and state == 1:
            ans_list.append(0)
            break
        elif op1 == 0 and state == 0:
            ans_list.append(0)
        else:
            ans_list.append(0)
            break
    for i in b[cur:]:
        ans_list.append(int(i))
    for i in ans_list:
        print(i, end="")
    print()
    print(ans)
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()
