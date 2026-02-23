from collections import defaultdict
from math import gcd

def maxPoints(points: list[list[int]]):
  if len(points) <= 2:
    return len(points)
  
  max_count = 0
  
  for i in range(len(points)):
    slopes = defaultdict(int)
    
    for j in range(i+1, len(points)):
      dy = points[j][1] - points[i][1]
      dx = points[j][0] - points[i][0]
      g = gcd(dy, dx)
      if g < 0:
          g = -g
      if dx < 0 or (dx == 0 and dy < 0):
          dy, dx = -dy, -dx
      slope = (dy // g, dx // g)
      
      slopes[slope] += 1
      max_count = max(max_count, slopes[slope])
  
  return max_count + 1

print(maxPoints([[1,1],[2,2],[3,3]]))
print(maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))