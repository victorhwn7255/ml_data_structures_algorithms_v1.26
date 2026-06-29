def removeDuplicates(nums: list[int]):
  left = 0
  right = 1
  
  while right < len(nums):
    if nums[left] != nums[right]:
      left += 1
      nums[left] = nums[right]
    right += 1
      
  return left+1