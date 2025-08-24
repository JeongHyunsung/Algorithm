S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    n = int(input())
    l = L()
    res = [0] * 20
    max_dist = [0] * 20
    for idx, i in enumerate(l):
        bin_i = bin(i)
        for j in range(len(bin_i)-2):
            cur = bin_i[len(bin_i)-1-j]
            if cur == '1':
                if max_dist[j] < idx+1 - res[j]:
                    max_dist[j] = idx+1-res[j]
                res[j] = idx+1
    for i in range(20):
        if res[i] != 0:
            if max_dist[i] < n+1 - res[i]:
                max_dist[i] = n+1-res[i]
    if n == 1:
        print(1)
    elif sum(l) == 0:
        print(1)
    else:
        ans = 0
        for i in range(20):
            if max_dist[i] != 0 and ans < max_dist[i]:
                ans = max_dist[i]
        print(ans)
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()