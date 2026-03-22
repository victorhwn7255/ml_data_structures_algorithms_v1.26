def merge(intervals: list[list[int]]):
  intervals.sort()
  result = [intervals[0]]
  
  for i in range(1, len(intervals)):
    current = intervals[i]
    last = result[-1]
    
    if current[0] <= last[1]:
      last[1] = max(last[1], current[1])
    else:
      result.append(current)
  
  return result

print(merge([[1,3],[2,6],[8,10],[15,18]]))
print(merge([[1,4],[4,5]]))