S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    n, k = S()
    l = L()
    l_copy = l[:]
    k -= 1
    h_idx = 0
    for i in range(k):
        if l[i] > l[k]:
            h_idx = i
            break
    ans = 0
    x = l[k]
    l[k] = l[h_idx]
    if h_idx != 0:
        ans += 1


    idx = h_idx + 1
    while idx < n and l[idx] < x:
        ans += 1
        idx += 1

    ans1 = 0
    l_copy[k] = l[0]
    idx = 1
    while idx < n and l[idx] < x:
        ans1 += 1
        idx += 1
    print(max(ans, ans1))
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()