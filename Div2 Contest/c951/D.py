S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    n, k = S()
    s = input() + "e"
    error = []
    cur = "s"
    srt, ln = 0, 0
    for idx, i in enumerate(s):
        if i != cur:
            if idx != 0 and ln != k:
                if idx == n:
                    error.append([cur, srt, ln, True])
                else:
                    error.append([cur, srt, ln, False])
            srt = idx
            ln = 1
            cur = i
        else:
            ln += 1
    if len(error) == 0: #clear
        print(n)
    elif len(error) == 1: #clear
        if s[-2] != error[0][0] and error[0][2] == 2 * k:
            print(error[0][1] + k)
        else:
            print(-1)
    elif len(error) == 2:
        if error[0][0] == error[1][0] and error[1][3] == True and error[1][2] + error[0][2] == 2*k and error[0][2] > error[1][2]:
            print(error[0][1] + (error[0][2]-k))
        elif error[0][0] == error[1][0] and error[1][3] == True and error[1][2] + error[0][2] == k:
            print(error[0][1] + error[0][2])
        else:
            print(-1)
    else:
        print(-1)
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()