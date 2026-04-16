def groupAnagrams(strs: list[str]):
  results = {}
  for word in strs:
    new_word = "".join(sorted(word))
    if new_word in results:
      results[new_word].append(word)
    else:
      results[new_word] = [word]
  
  return list(results.values())

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))