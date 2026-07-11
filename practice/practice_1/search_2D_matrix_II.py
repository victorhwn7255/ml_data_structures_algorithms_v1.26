def searchMatrix(matrix: list[list[int]], target: int):
  rows = len(matrix)
  cols = len(matrix[0])
  
  col = cols - 1
  row = 0
  
  while 0<= col < cols and 0<= row < rows:
    if matrix[row][col] < target:
      row += 1
    elif matrix[row][col] > target:
      col -= 1
    else:
      return True
  
  return False