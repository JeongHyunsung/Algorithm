S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    n = int(input())
    l = L()
    counter = [0] * (n+1)
    for i in l:
        counter[i] += 1
    ans = 0
    cnt = 0
    for idx, i in enumerate(counter):
        if i == 0:
            cnt = 2
        if i == 1:
            cnt += 1
        if cnt == 2:
            ans = idx
            break
        


    print(ans)
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()

