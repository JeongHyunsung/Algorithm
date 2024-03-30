S = lambda : map(int, input().split())
L = lambda : list(S())


if __name__ == "__main__":
    ms = {}
    for i in range(30):
        ms[i] = 0

    for query in range(int(input())):

        t, v = S()
        if t == 1:
            ms[v] += 1
        else:
            for i in range(29, -1, -1):
                pos = min(v//(2**i), ms[i])
                v -= pos * (2**i)
            if v:
                print("NO")
            else:
                print("YES")



            




