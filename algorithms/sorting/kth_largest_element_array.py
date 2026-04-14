import heapq

def findKthLargest(nums: list[int], k: int):
  results = []
  
  for num in nums:
    heapq.heappush(results, num)
    if len(results) > k:
      heapq.heappop(results)
  
  return results[0]


print(findKthLargest([3,2,1,5,6,4], 2))