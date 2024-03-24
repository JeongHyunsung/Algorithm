def solve():
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    l_m = []
    for i in range(n-1):
        l_m.append(abs(l[i+1]-l[i]))
    l_m.sort(reverse=True)
    print(sum(l_m[k-1:]))
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()
        