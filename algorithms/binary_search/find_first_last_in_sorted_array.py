def searchRange(nums: list[int], target: int):
  
  return [findLeft(nums, target), findRight(nums, target)]

def findLeft(nums, target):
  left = 0
  right = len(nums) - 1
  result = -1
  
  while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
      result = mid
      right = mid - 1
    elif nums[mid] < target:
      left = mid + 1
    else:
      right = mid - 1
  
  return result

def findRight(nums, target):
  left = 0
  right = len(nums) - 1
  result = -1
  
  while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
      result = mid
      left = mid + 1
    elif nums[mid] < target:
      left = mid + 1
    else:
      right = mid -1
  
  return result


print(searchRange([5,7,7,8,8,10], 8))
print(searchRange([5,7,7,8,8,10], 6))