from collections import deque

def bfs(x, y, graph):
    queue = deque([(x, y, 0)])
    visit = []
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while queue:
        n = queue.popleft()
        nx, ny, dist = n[0], n[1], n[2]
        loc = (nx, ny)
        if loc not in visit:
            visit.append(loc)
            if 0 <= nx < 5 and 0 <= ny < 5 and dist <= 2:
                if graph[nx][ny] != 'X':
                    if dist > 0 and graph[nx][ny] == 'P':
                        return False
                    else:
                        for i in range(4):
                            queue.append((nx+dx[i], ny+dy[i], dist+1))
    return True

def check(graph):
    for i in range(5):
        for j in range(5):
            if graph[i][j] == 'P':
                if not bfs(i, j, graph):
                    return False
    return True

def solution(places):
    answer = [1] * 5
    for p in range(5):
        graph = [list(place) for place in places[p]]
        if not check(graph):
            answer[p] = 0

    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))