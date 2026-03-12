def minPathSum(grid: list[list[int]]):
  rows = len(grid)
  cols = len(grid[0])
  n = rows * cols
  
  dp = [[0] * cols for _ in range(rows)]
  
  dp[0][0] = grid[0][0]
  
  for col in range(1, cols):
    dp[0][col] = dp[0][col-1] + grid[0][col]
    
  for row in range(1, rows):
    dp[row][0] = dp[row-1][0] + grid[row][0]
  
  for row in range(1, rows):
    for col in range(1, cols):
      dp[row][col] = grid[row][col] + min(dp[row-1][col], dp[row][col-1])
  
  return dp[rows-1][cols-1]


print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
print(minPathSum([[1,2,3],[4,5,6]]))