class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seth = set()
            setv = set()
            for j in range (9):
                eleh = board[i][j]
                elev = board[j][i]
                if (eleh != "."):
                    if eleh not in seth:
                        seth.add(eleh)
                    else:
                        return False
                if (elev != "."):
                    if elev not in setv:
                        setv.add(elev)
                    else:
                        return False
        squares =  defaultdict(set)
        for i in range (9):
            for j in range (9):
                if (board[i][j]=="."):
                    continue
                if (board[i][j] not in squares[(i//3),j//3]):
                    squares[(i//3),j//3].add(board[i][j])
                else:
                    return False
        return True    
        