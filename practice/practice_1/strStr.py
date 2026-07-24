def strStr(haystack: str, needle: str):
  start = needle[0]
  n = len(needle)
  
  for index, char in enumerate(haystack):
    if char == start:
      new_string = haystack[index:index+n]
      if new_string == needle:
        return index
  
  return -1