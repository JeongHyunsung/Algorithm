S = lambda: map(int, input().split())
L = lambda: list(S())

def solve():
    a, b = S()
    flag = 0
    if a % 2 == 0 and a != 2 * b:
        flag = 1
    if b % 2 == 0 and b != 2 * a:
        flag = 1
    if flag:
        print("YES")
    else:
        print("NO")
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()
