def twoSum(nums: list[int], target: int):
  diff_table = {}
  
  for (i, num) in enumerate(nums):
    diff = target - num
    if diff in diff_table:
      return [diff_table[diff], i]
    else:
      diff_table[num] = i
      
      
print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))