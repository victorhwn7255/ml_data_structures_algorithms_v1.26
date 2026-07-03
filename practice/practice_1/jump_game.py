def canJump(nums: list[int]):
  furthest = nums[0]
  length = len(nums)
  
  for i in range(1, length):
    if furthest == 0:
      return False
    
    furthest = max(furthest-1, nums[i])
  
  return True

print(canJump([3,2,1,0,4]))