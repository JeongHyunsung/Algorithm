S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    n = int(input())
    l = L()
    ll = []
    for i in range(n-1):
        ll.append(max(l[i], l[i+1]))
    print(min(ll)-1)
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()