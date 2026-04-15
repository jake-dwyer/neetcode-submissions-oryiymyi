class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = {}

            for col in range(9):
                value = board[row][col]

                if value == ".":
                    continue

                if value in seen:
                    return False

                seen[value] = True


        for col in range(9):
            seen = {}

            for row in range(9):
                value = board[row][col]

                if value == ".":
                    continue

                if value in seen:
                    return False

                seen[value] = True
        
        for box in range(9):
            seen = {}

            for i in range(3):
                for j in range(3):
                    row = (box // 3) * 3 + i
                    col = (box % 3) * 3 + j
                    value = board[row][col]

                    if value == ".":
                        continue
                    
                    if value in seen:
                        return False
                    
                    seen[value] = True
        return True

