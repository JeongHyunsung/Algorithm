S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    n, x, y = S()
    l = L()
    ans = n-2
    gap_list = []
    l.sort()

    for i in range(x-1):
        gap = l[i+1] - l[i]
        if gap >= 3:
            gap_list.append(gap)
            ans -= (gap - 1)
    gap = l[0] + n - l[-1]
    if gap >= 3:
        gap_list.append(gap)
        ans -= (gap - 1)

    # 여기까지 뺐고 이제부터 더하기 
    
    even = []
    for i in gap_list:
        if i % 2 == 0:
            even.append(i)
    even.sort(reverse=True)

    while y > 0 and len(even) > 0:
        cur = even.pop()
        if cur//2 - 1 > y:
            ans += y*2
            y = 0
            break
        else:
            ans += (cur-1)
            y -= (cur//2 -1)
    if y > 0:
        ans += 2 * y
    if ans > n-2:
        ans = n-2
    print(ans)
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()

# 한칸 뛰어넘는건 괜찮고 2~3개부터 그 개수만큼 삼각형 개수 차감