def searchRange(nums: list[int], target:int):
  left_most = -1
  right_most = -1
  
  left, right = 0, len(nums) - 1
  while left <= right:
    mid = (left + right) // 2
    if nums[mid] < target:
      left = mid + 1
    elif nums[mid] > target:
      right = mid - 1
    else:
      right_most = mid
      left = mid + 1
  
  left, right = 0, len(nums) - 1 
  while left <= right:
    mid = (left + right) // 2
    if nums[mid] < target:
      left = mid + 1
    elif nums[mid] > target:
      right = mid - 1
    else:
      left_most = mid
      right = mid - 1
  
  
  return [left_most, right_most]