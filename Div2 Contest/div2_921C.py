S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    n, k, m = S()
    s = input()
    a_ord = ord("a")
    ans = ""
    cnt = 0
    flag = [0] * k
    for i in s:
        flag[ord(i)-a_ord] = 1
        if sum(flag) == k:
            cnt += 1
            ans += i
            flag = [0] * k
    if cnt >= n:
        print("YES")
    else:
        er_chr = "a"
        for idx, i in enumerate(flag):
            if i == 0:
                er_chr = chr(a_ord+idx)
        print("NO")
        print(ans+er_chr+"a"*(n-cnt-1))
                

if __name__ == "__main__":
    for test in range(int(input())):
        solve()
