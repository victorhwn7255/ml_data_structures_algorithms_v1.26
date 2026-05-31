def twoSum(nums: list[int], target: int):
  hash_map = {}
  
  for i in range(len(nums)):
    diff = target - nums[i]
    if diff in hash_map:
      return [i, hash_map[diff]]
    else:
      hash_map[nums[i]] = i
  

print(twoSum([2,7,11,15], 9))