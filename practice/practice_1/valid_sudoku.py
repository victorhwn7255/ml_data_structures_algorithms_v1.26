def isValidSudoku(board:list[list[str]]):
  row_checks = [set() for _ in range(9)]
  col_checks = [set() for _ in range(9)]
  box_checks = [set() for _ in range(9)]
  
  for row in range(9):
    for col in range(9):
      current = board[row][col]
      box_index = (row // 3) * 3 + (col // 3)
      
      if current == ".":
        continue
      
      if current in row_checks[row] or current in col_checks[col] or current in box_checks[box_index]:
        return False

      row_checks[row].add(current)
      col_checks[col].add(current)
      box_checks[box_index].add(current)
  
  return True