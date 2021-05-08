import sys
sys.setrecursionlimit(10000000)

def getCursorUP(k, up):
    if k in up:
        up[k] = getCursorUP(up[k], up)
        return up[k]
    else:
        return k

def getCursorDOWN(k, down):
    if k in down:
        down[k] = getCursorDOWN(down[k], down)
        return down[k]
    else:
        return k

def restoreCursor(t, up, down):
    tempUp = t + 1
    tempDown = t - 1
    while tempUp in up:
        up[tempUp] = t
        tempUp += 1
    while tempDown in down:
        down[tempDown] = t
        tempDown -= 1
    del up[t]
    del down[t]

def solution(n, k, cmd):
    answer = ['O' for _ in range(n)]
    d = []
    down = {}
    up = {}
    for cm in cmd:
        c = cm.split()
        if c[0] == 'U':
            for _ in range(int(c[1])):
                k = getCursorUP(k - 1, up)
        elif c[0] == 'D':
            for _ in range(int(c[1])):
                k = getCursorDOWN(k + 1, down)
        elif c[0] == 'C':
            up[k] = k - 1
            down[k] = k + 1
            answer[k] = 'X'
            d.append(k)
            temp = getCursorDOWN(k + 1, down)
            if temp < n:
                k = temp
            else:
                k = getCursorUP(k - 1, up)
        else:
            t = d.pop()
            restoreCursor(t, up, down)
            answer[t] = 'O'

    return ''.join(answer)

n = 8
k = 4
cmd = ["C","C","C","U 1","D 1"]
print(solution(n, k, cmd))