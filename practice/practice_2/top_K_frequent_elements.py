import heapq

def topKFrequent(nums: list[int], k: int):
  hash_map = {}
  heap = []
  
  for num in nums:
    hash_map[num] = hash_map.get(num, 0) + 1
  
  for num, freq in hash_map.items():
    heapq.heappush(heap, (freq, num))
    if len(heap) > k:
      heapq.heappop(heap)
  
  results = []
  while heap:
    freq, num = heapq.heappop(heap)
    results.append(num)
  
  return results

