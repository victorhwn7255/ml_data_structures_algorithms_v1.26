def intersect(nums1: list[int], nums2: list[int]):
  hash_map = {}
  results = []
  
  for num in nums1:
    hash_map[num] = hash_map.get(num, 0) + 1
  
  for num in nums2:
    if num in hash_map and hash_map[num] >= 1:
      results.append(num)
      hash_map[num] -= 1
  
  return results


print(intersect([4,9,5], [9,4,9,8,4]))