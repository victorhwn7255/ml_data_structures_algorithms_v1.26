def twoSum(nums: list[int], target: int):
  seen = {}
  
  for i, num in enumerate(nums):
    diff = target - num
    if diff in seen:
      return [seen[diff], i]
    else:
      seen[num] = i
    
print(twoSum([2,7,11,15], 9))
print(twoSum([3, 2, 4], 6))
