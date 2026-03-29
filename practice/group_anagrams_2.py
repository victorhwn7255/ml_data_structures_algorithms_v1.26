def groupAnagrams(strs: list[str]):
  results = {}
  
  for word in strs:
    key = "".join(sorted(word))
    if key not in results:
      results[key] = [word]
    else:
      results[key].append(word)
  
  return list(results.values())


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))