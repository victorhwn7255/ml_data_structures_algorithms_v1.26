def merge(intervals: list[list[int]]):
  sorted_list = sorted(intervals)
  results = [sorted_list[0]]
  
  for i in range(1, len(sorted_list)):
    current = sorted_list[i]
    if results[-1][1] >= current[0]: #overlap
      results[-1][1] = max(results[-1][1], current[1])
    else:   #non-overlap
      results.append(current)
  
  return results


print(merge([[1,3],[2,6],[8,10],[15,18]]))
print(merge([[4,7],[1,4]]))