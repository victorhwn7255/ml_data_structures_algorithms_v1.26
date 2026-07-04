def isAnagram(s: str, t: str):
  hash_map = {}
  
  if len(s) != len(t):
    return False
  
  for char in s:
    hash_map[char] = hash_map.get(char, 0) + 1
    
  for char in t:
    if char not in hash_map:
      return False
    else:
      hash_map[char] -= 1
  
  return all(value == 0 for value in hash_map.values())