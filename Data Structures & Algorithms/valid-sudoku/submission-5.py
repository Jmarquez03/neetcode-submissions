class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def gridPosition(row: int, col: int) -> int:
            if col < 3:
                if row < 3:
                    return 0
                elif row < 6:
                    return 3
                else:
                    return 6
            elif col < 6:
                if row < 3:
                    return 1
                elif row < 6:
                    return 4
                else:
                    return 7
            else:
                if row < 3:
                    return 2
                elif row < 6:
                    return 5
                else: 
                    return 8
        # Initial thoughts: Create a dictionary of each row and column with a set as each key
        columns = {}
        rows = {}
        grids = {}
        for i in range(9):
            columns[i] = set()
            rows[i] = set()
            grids[i] = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                num = board[i][j]
                if(num == "."):
                    continue
                gridPos = gridPosition(i, j)
                if num in columns[j] or num in rows[i] or num in grids[gridPos]:
                    return False
                else:
                    columns[j].add(num)
                    rows[i].add(num)
                    grids[gridPos].add(num)
        return True

                
        # We can also create a set with each 3x3 grid
