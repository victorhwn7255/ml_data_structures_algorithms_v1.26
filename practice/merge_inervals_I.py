def merge(intervals: list[list[int]]):
  intervals.sort()
  result = [intervals[0]]
  
  for i in range(1, len(intervals)):
    current = result[-1]
    if intervals[i][0] <= current[1]: #overlap
      current[1] = max(current[1], intervals[i][1])
    else: #not overlap
      result.append(intervals[i])
  
  return result


print(merge([[1,3],[2,6],[8,10],[15,18]]))