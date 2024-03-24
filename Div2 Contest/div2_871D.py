def solve():
    a, b = map(int, input().split())
    ans = 0
    if a == b:
        ans = 1
    for i in range(1, 100):
        if a % 3 != 0:
            break
        else:
            a //= 3
            for j in range(0, i+1):
                if a * 2 ** j == b:
                    ans = 1
    if ans:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    for test in range(int(input())):
        solve()
        