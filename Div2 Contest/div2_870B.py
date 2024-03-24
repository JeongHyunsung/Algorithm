if __name__ == "__main__":
    for test in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        if n == 1:
            print(0)
        else:
            b = []
            for i in range(n//2):
                b.append(abs(a[n-1-i] - a[i]))
            ans = 0
            for i in b:
                i_m = i
                while ans * i_m:
                    ma = max(ans, i_m)
                    mi = min(ans, i_m)
                    ma = ma % mi
                    ans = ma
                    i_m = mi
                ans = max(ans, i_m)
            print(ans)
            
