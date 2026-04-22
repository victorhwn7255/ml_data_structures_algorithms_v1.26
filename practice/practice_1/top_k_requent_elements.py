import heapq

def topKFrequent(nums: list[int], k: int):
  freq_count = {}
  for num in nums:
    if num in freq_count:
      freq_count[num] += 1
    else:
      freq_count[num] = 1
  
  heap = []
  for key, value in freq_count.items():
    heapq.heappush(heap, (value, key))
    if len(heap) > k:
      heapq.heappop(heap)
  
  results = []
  for item in heap:
    results.append(item[1])
  return results


print(topKFrequent([1,2,1,2,1,2,3,1,3,2], 2))