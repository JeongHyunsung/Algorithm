S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    n = int(input())
    nc = n
    ans_1 = 0


    ans_1 += nc // 15
    nc %= 15

    if ans_1 >= 1:
        ans_1 -= 1
        nc += 15
    if nc == 20 or nc == 12:
        print(ans_1+2)
        return
    if nc == 23 or nc == 27:
        print(ans_1+3)
        return
    ans_1 += nc // 15
    nc %= 15
    ans_1 += nc // 10
    nc %= 10
    ans_1 += nc // 6
    nc %= 6
    ans_1 += nc // 3
    nc %= 3
    ans_1 += nc
    print(ans_1)
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()
