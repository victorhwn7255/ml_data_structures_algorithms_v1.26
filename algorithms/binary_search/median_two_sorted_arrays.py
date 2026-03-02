def findMedianSortedArrays(nums1: list[int], nums2: list[int]):
  if len(nums1) > len(nums2):
    nums1, nums2 = nums2, nums1
    
  m = len(nums1)
  n = len(nums2)
  half = (m + n + 1) // 2
  left = 0
  right = m
  
  while left <= right:
    i = (left + right) // 2
    j = half - i

    a1 = nums1[i - 1] if i > 0 else float('-inf')
    b1 = nums1[i] if i < m else float('inf')
    a2 = nums2[j-1] if j > 0 else float('-inf')
    b2 = nums2[j] if j < n else float('inf')
    
    if a1 > b2:
      right = i - 1
    elif a2 > b1:
      left = i + 1
    else:
      max_left = max(a1, a2)
      min_right = min(b1, b2)
      
      if (m + n) % 2 == 1:
        return max_left
      else:
        return (max_left + min_right) / 2


print(findMedianSortedArrays([1, 3], [2]))
print(findMedianSortedArrays([1, 2], [3, 4]))