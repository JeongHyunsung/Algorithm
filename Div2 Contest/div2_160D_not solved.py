S = lambda : map(int, input().split())
L = lambda : list(S())


def solve():
    n = int(input())
    l = L()
    l_max = []
    for i in range(n-1):
        l_max.append(max(l[i], l[i+1]))
    counter = {}
    for i in l_max:
        if i not in counter.keys():
            counter[i] = 1
        else:
            counter[i] += 1
    ans = 1
    for i in counter.keys():
        if counter[i] == 2:
            ans *= 3
        else:
            ans *= 2
    print(ans % 998244353)


    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()
