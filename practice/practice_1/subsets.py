def subsets(nums: list[int]):
  results = []
  
  def backtrack(start_index, current_subset: list[int]):
    results.append(current_subset.copy())
    
    for i in range(start_index, len(nums)):
      current_subset.append(nums[i])
      backtrack(i+1, current_subset)
      current_subset.pop()
  
  backtrack(0, [])
  return results