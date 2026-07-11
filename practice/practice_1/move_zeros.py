def moveZeroes(nums: list[int]):
  num_index = 0
  
  for i in range(len(nums)):
    if nums[i] != 0:
      nums[num_index], nums[i] = nums[i], nums[num_index]
      num_index += 1
  
