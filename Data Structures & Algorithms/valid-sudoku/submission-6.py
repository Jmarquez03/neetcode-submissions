class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # You can use floor division and tuples for grid position
        columns = defaultdict(set)
        rows = defaultdict(set)
        grids = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[i])):
                num = board[i][j]
                if(num == "."):
                    continue
                gridPos = (i//3, j//3)
                if num in columns[j] or num in rows[i] or num in grids[gridPos]:
                    return False
                else:
                    columns[j].add(num)
                    rows[i].add(num)
                    grids[gridPos].add(num)
        return True

                
        # We can also create a set with each 3x3 grid
