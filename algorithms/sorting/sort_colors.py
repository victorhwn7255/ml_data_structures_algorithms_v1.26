def sortColors(nums: list[int]):
  low = 0
  mid = 0
  high = len(nums)-1
  
  while mid <= high:
    if nums[mid] == 0:
      temp = nums[low]
      nums[low] = 0
      nums[mid] = temp
      low += 1
      mid += 1
    elif nums[mid] == 1:
      mid += 1
    else:
      temp = nums[high]
      nums[high] = 2
      nums[mid] = temp
      high -= 1
  

print(sortColors([2,0,2,1,1,0]))