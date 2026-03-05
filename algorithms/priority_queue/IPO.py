import heapq

def findMaximizedCapital(k: int, w: int, profits: list[int], capital: list[int]):
  min_heap = []
  for i in range(len(profits)):
    heapq.heappush(min_heap, (capital[i], profits[i]))
    
  max_heap = []
  for _ in range(k):
    while min_heap and min_heap[0][0] <=w:
      cap, profit = heapq.heappop(min_heap)
      heapq.heappush(max_heap, -profit)
  
    if not max_heap:
      break
    
    w += -heapq.heappop(max_heap)
  
  return w


print(findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]))
print(findMaximizedCapital(3, 0, [1, 2, 3], [0, 1, 2]))