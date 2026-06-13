class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        sqar = defaultdict(set)
        for i in range (9):
            for j in range (9):
                if board[i][j] == ".":
                    continue
                else:
                    ele = board[i][j]
                    if ele in rows[i] or ele in cols[j] or ele in sqar[(i//3,j//3)]:
                        return False
                    else:
                        rows[i].add(ele)
                        cols[j].add(ele)
                        sqar[(i//3,j//3)].add(ele)
        return True
                    
                        
