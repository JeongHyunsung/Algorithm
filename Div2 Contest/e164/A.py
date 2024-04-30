S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    n, m, k = S()
    most_common_number_min = n // m 
    if n % m != 0:
        most_common_number_min += 1
    else_max = n - most_common_number_min
    if k < else_max:
        print("YES")
    else:
        print("NO")
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()