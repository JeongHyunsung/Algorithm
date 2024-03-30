S = lambda: map(int, input().split())
L = lambda: list(S())
import math

def solve():
    n = int(input())
    l = L()
    cur_mcd = 0 
    for i in range(n-1):
        cur_num = abs(l[i+1]-l[i])
        cur_mcd = math.gcd(cur_num, cur_mcd)
    if cur_mcd == 0:
        print(1)
        return
    mx = max(l)
    det = [0] * 200001
    ans = 0
    for i in range(n):
        ct = (mx-l[i])//cur_mcd
        ans += ct
        if ct >= 0 and ct <= 200000:
            det[ct] = 1
    ans_num = -1
    for i in range(200001):
        if det[i] != 1:
            ans_num = i
            break
    ans += ans_num
    print(ans)
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()

