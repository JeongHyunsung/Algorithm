if __name__ == "__main__":
    for test in range(int(input())):
        n = int(input())
        l = list(map(int, input().split()))
        for i in range(n+1):
            cnt = 0
            for j in range(n):
                if l[j] > i:
                    cnt += 1
            if cnt == i:
                ans = i
                break
        print(ans)
