def rotate(matrix: list[list[int]]):
  rows = len(matrix)
  cols = len(matrix[0])
  
  for row in range(rows):
    for col in range(row+1, cols):
      matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
  
  for row in range(rows):
    left = 0
    right = cols-1
    
    while left < right:
      matrix[row][left], matrix[row][right] = matrix[row][right], matrix[row][left]
      left += 1
      right -= 1
  



