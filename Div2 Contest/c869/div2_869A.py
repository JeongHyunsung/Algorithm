S = lambda: map(int, input().split())
L = lambda: list(map(int, input().split()))


def solve():
    n, k = S()
    l = []
    for i in range(n):
        l.append(input())

    cnt = 0
    for i in l[1:]:
        if i == l[0]:
            cnt += 1
    print(cnt + 1)
    return

if __name__ == "__main__":
    for test in range(int(input())):
        solve()
