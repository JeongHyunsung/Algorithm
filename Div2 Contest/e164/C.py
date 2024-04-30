S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    a = list(map(int, list(input())))
    b = list(map(int, list(input())))
    flag = True
    for i in range(len(a)):
        if flag:
            if a[i] == b[i]:
                continue
            elif a[i] < b[i]:
                mem = a[i]
                a[i] = b[i]
                b[i] = mem
                flag = False
            else:
                flag = False
        else:
            if a[i] > b[i]:
                mem = a[i]
                a[i] = b[i]
                b[i] = mem
    for i in a:
        print(i, end="")
    print()
    for i in b:
        print(i, end="")
    print()

    

    
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()