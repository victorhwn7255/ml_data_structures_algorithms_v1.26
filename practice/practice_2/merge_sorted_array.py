def merge(nums1: list[int], m: int, nums2: list[int], n: int):
  one = m - 1
  two = n - 1
  current = m + n - 1
  
  while one >=0 and two >=0:
    if nums1[one] >= nums2[two]:
      nums1[current] = nums1[one]
      one -= 1
    else:
      nums1[current] = nums2[two]
      two -= 1
    current -= 1
    
  while two >= 0:
    nums1[current] = nums2[two]
    two -= 1
    current -= 1
  