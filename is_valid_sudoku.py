"""
Using hash set for "each ROW, each COLUMN, each SQUARE"
"""

from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check_rows, check_cols, check_box = False, False, False
        # cols_map, box_map = {}, {}
        # for row in board:
        #     rows_map = {}
        #     for i in row:
        #         if i != ".":
        #             if i in rows_map:
        #                 return False
        #             rows_map[i] = True
        # check_rows = True

        # # checking for columns
        # rows = len(board)
        # cols = len(board[0])
        # for row in range(rows):
        #     cols_map = {}
        #     for col in range(cols):
        #         if board[col][row] != ".":
        #             if board[col][row] in cols_map:
        #                 return False
        #             cols_map[board[col][row]] = True
        #     print(cols_map)
        # check_cols = True

        # return check_rows and check_cols

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        rows_len = len(board)
        cols_len = len(board[0])
        for i in range (rows_len):
            for j in range(cols_len):
                if board[i][j] != ".":
                    if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in squares[(i//3, j//3)]:
                        return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[(i//3, j//3)].add(board[i][j])
        
        return True




                

                    


            

        