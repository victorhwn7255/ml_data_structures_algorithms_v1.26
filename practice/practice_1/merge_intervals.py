def merge(intervals: list[list[int]]):
  intervals.sort()
  results = [intervals[0]]
  
  for i in range(1, len(intervals)):
    current = intervals[i]
    if results[-1][1] >= current[0]: #OVERLAP
      results[-1][1] = max(results[-1][1], current[1])
    else: #NOT OVERLAP
      results.append(current)
  
  return results