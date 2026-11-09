class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        boxes = {}

        for row in range(9):
            for col in range(9):
                if row not in rows:
                    rows[row] = set()
                if col not in cols:
                    cols[col] = set()
                box_row = row//3
                box_col = col//3
                if (box_row,box_col) not in boxes:
                    boxes[(box_row,box_col)] = set()
                

                if board[row][col] != ".":
                    if board[row][col] not in boxes[(box_row,box_col)]:
                        boxes[(box_row,box_col)].add(board[row][col])
                    else:
                        return False

                    if board[row][col] not in cols[col]:
                        cols[col].add(board[row][col])
                    else:
                        return False

                    if board[row][col] not in rows[row]:
                        rows[row].add(board[row][col])
                    else:
                        return False

        return True

