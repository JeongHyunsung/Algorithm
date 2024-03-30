def solve():
    smp = "codeforces"
    a = input()
    cnt = 0
    for i in range(10):
        if smp[i] == a[i]:
            cnt += 1
    print(10-cnt)
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()
        