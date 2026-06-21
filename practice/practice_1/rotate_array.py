def rotate(nums: list[int], k: int):
  n = len(nums)
  k %= n
  
  front = nums[n-k:n]
  back = nums[0:n-k]
  
  nums[:] = front + back

