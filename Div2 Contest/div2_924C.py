S = lambda: map(int, input().split())
L = lambda: list(S())

def solve():
    n, x = S()
    min_div = 2*x-2
    
    if x > n:
        print(0)
    else:
        num_lst = [n+x-2, n-x]

        num_div_lst = []
        for num in num_lst:
            a = num
            d = []
            large_d = []
            for i in range(1, int(n**0.5+1)):
                if a % i == 0:
                    
                    if i >= min_div and i%2 == 0:
                        d.append(i)
                    if i**2 != a:
                        if a//i >= min_div and (a//i)%2 == 0:
                            large_d.append(a//i)
            for i in reversed(large_d):
                d.append(i)
            num_div_lst.extend(d)
        ans = list(set(num_div_lst))

        print(len(ans))
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()
