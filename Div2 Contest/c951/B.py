S = lambda: map(int, input().split())
L = lambda: list(S())


def solve():
    a, b = S()
    a = bin(a)[2:]
    b = bin(b)[2:]
    cnt = 0
    for i in range(min(len(a), len(b))):
        if a[-1 * (i+1)] == b[-1 * (i+1)]:
            cnt += 1
            if i == len(a)-1:
                srt = i+1
                while srt <= len(b)-1 and b[-1 * (srt+1)] == '0':
                    cnt += 1
                    srt += 1
            if i == len(b)-1:
                srt = i+1
                while srt <= len(a)-1 and a[-1 * (srt+1)] == '0':
                    cnt += 1
                    srt += 1
                    
        else:
            break
    print(2 ** cnt)
    return


if __name__ == "__main__":
    for test in range(int(input())):
        solve()