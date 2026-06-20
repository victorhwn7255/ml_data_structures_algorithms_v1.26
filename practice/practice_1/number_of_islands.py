def numIslands(grid:list[list[str]]):
  count = 0
  visited = set()
  
  def dfs(row, col):
    if (
      row < 0 or row >= len(grid) or
      col < 0 or col >= len(grid[0]) or 
      grid[row][col] == "0" or
      (row, col) in visited
    ):
      return
    
    visited.add((row, col))
    dfs(row+1, col)
    dfs(row-1, col)
    dfs(row, col+1)
    dfs(row, col-1)
  
  for row in range(len(grid)):
    for col in range(len(grid[0])):
      if grid[row][col] == "1" and (row, col) not in visited:
        count += 1
        dfs(row, col)
  
  return count


grid_test_1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid_test_2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(numIslands(grid_test_1))
print(numIslands(grid_test_2))