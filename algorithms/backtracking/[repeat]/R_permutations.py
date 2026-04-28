def permute(nums: list[int]):
  results = []
  
  def backtrack(path: list, used):
    if len(path) == len(nums):
      results.append(path.copy())
      return
    
    for i in range(len(nums)):
      if used[i]:
        continue
      used[i] = True
      path.append(nums[i])
      backtrack(path, used)
      path.pop()
      used[i] = False
    
  backtrack([], [False]*len(nums))
  return results

print(permute([1, 2, 3]))

