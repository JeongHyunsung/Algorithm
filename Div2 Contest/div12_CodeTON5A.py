def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if sum(a) == sum(b):
        print("Draw")
    elif sum(a) > sum(b):
        print("Tsondu")
    else:
        print("Tenzing")
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()