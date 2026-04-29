def searchRange(nums: list[int], target: int):
  if len(nums) == 0:
    return [-1, -1]
  
  def findLeftMost(nums, target):
    result = -1
    left = 0
    right = len(nums) - 1
    
    while left <= right:
      mid = (left + right) // 2
      if nums[mid] > target:
        right = mid - 1 
      elif nums[mid] < target:
        left = mid + 1
      else:
        result = mid
        right = mid - 1
    
    return result
  
  def findRightMost(nums, target):
    result = -1
    left = 0
    right = len(nums) - 1
    
    while left <= right:
      mid = (left + right) // 2
      if nums[mid] > target:
        right = mid - 1 
      elif nums[mid] < target:
        left = mid + 1
      else:
        result = mid
        left = mid + 1
    
    return result
        
  left_pos = findLeftMost(nums, target) 
  
  if left_pos == -1:
    return [-1, -1]
   
  right_pos = findRightMost(nums, target)
    
  return [left_pos, right_pos]

