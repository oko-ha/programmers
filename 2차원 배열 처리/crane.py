def solution(board, moves):
    answer = 0
    temp = []
    for move in moves:
        for y in range(len(board)):
            if board[y][move - 1] != 0:
                if len(temp) != 0 and \
                temp[-1] == board[y][move - 1]:
                        answer += 2
                        temp.pop()
                else:
                    temp.append(board[y][move - 1])
                board[y][move - 1] = 0
                break
            
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))
