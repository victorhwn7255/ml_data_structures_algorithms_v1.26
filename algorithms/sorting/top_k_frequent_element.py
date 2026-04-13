import heapq

def topKFrequent(nums: list[int], k: int):
  hash_map = {}
  
  for num in nums:
    if num in hash_map:
      hash_map[num] += 1
    else:
      hash_map[num] = 1
  
  heap = []
  for num, freq in hash_map.items():
    heapq.heappush(heap, (freq, num))
    if len(heap) > k:
      heapq.heappop(heap)
  
  results = []
  for (freq, num) in heap:
    results.append(num)
  
  return results


print(topKFrequent([1,1,1,2,2,3], 2))