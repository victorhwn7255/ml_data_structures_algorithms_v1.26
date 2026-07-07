def exist(board: list[list[str]], word: str):
  DIRECTIONS = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1]
  ]
  
  rows = len(board)
  cols = len(board[0])
  
  def backtrack(row, col, index=0):
    if index == len(word):
      return True
    
    if row < 0 or row >= rows or col < 0 or col >= cols:
      return False
    
    current_char = board[row][col]
    if current_char != word[index]:
      return False
    
    board[row][col] = "#"
    for dr, dc in DIRECTIONS:
      if backtrack(row + dr, col + dc, index + 1):
        board[row][col] = current_char
        return True
    
    board[row][col] = current_char
    return False
  
  for row in range(rows):
    for col in range(cols):
      if backtrack(row, col, 0):
        return True
  
  return False