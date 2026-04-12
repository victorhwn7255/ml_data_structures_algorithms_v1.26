BAD_VERSION = 4

def isBadVersion(version: int) -> bool:
    return version >= BAD_VERSION

def firstBadVersion(n: int):
  left = 1
  right = n
  
  while left <= right:
    mid = (left + right) // 2
    if isBadVersion(mid):
      right = mid - 1
    else:
      left = mid + 1
  
  return left

