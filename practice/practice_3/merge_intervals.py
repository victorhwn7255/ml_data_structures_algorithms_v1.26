def merge(intervals: list[list[int]]):
  intervals.sort()
  results = [intervals[0]]
  for item in intervals:
    current = results[-1]
    if item[0] <= current[1]: #OVERLAP
      results[-1][1] = max(item[1], current[1])
    else: #NON-OVERLAP
      results.append(item)
  
  return results


print(merge([[1,3],[2,6],[8,10],[15,18]]))

