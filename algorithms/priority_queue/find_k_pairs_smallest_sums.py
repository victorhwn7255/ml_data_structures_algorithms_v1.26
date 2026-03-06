import heapq

def kSmallestPairs(nums1: list[int], nums2: list[int], k: int):
  heap = []
  results = []
  
  for j in range(min(len(nums2), k)):
    heapq.heappush(heap, (nums1[0] + nums2[j], 0, j))
  
  while heap and k>0:
    total, i, j = heapq.heappop(heap)
    results.append([nums1[i], nums2[j]])
    k -= 1
    
    if i + 1 < len(nums1):
      heapq.heappush(heap, (nums1[i+1] + nums2[j], i+1, j))
  
  return results

print(kSmallestPairs([1,7,11], [2,4,6], 3))
print(kSmallestPairs([1,1,2], [1,2,3], 2))