def solution(board):
    result = 0
    hei,wid = len(board),len(board[0])
    for i in range(hei):
        for j in range(wid):
            if board[i][j] == 1: 
                for a,b in [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]:
                    if 0<=i+a<hei and 0<=j+b<wid and board[i+a][j+b] == 0: board[i+a][j+b] = 2
    for i in board: result += i.count(0)
    return result

print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]))