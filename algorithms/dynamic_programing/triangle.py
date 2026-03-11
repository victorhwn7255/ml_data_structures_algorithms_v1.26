def minimumTotal(triangle: list[list[int]]):
  n = len(triangle)
  dp = triangle[n-1]
  
  for row in range(n-2, -1, -1):
    for i in range(len(triangle[row])):
      dp[i] = triangle[row][i] + min(dp[i], dp[i+1])
  
  return dp[0]

print(minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
print(minimumTotal([[-10]]))
print(minimumTotal([[2],[4,8],[7,6,5],[8,4,2,9]]))