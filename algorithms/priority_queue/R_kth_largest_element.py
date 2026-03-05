import heapq

def findKthLargest(nums: list[int], k:int):
  heap = []
  for num in nums:
    heapq.heappush(heap, num)
    if len(heap) > k:
      heapq.heappop(heap)
  
  return heap[0]

print(findKthLargest([3,2,1,5,6,4], 2))
print(findKthLargest([3,2,3,1,2,4,5,5,6], 4))