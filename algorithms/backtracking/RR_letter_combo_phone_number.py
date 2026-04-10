def letterCombinations(digits: str):
  if not digits:
    return []
  
  results = []
  digits_dict = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
  }
  
  def backtrack(index, path: list):
    if index == len(digits):
      results.append(''.join(path))
      return
    
    for char in digits_dict[digits[index]]:
      path.append(char)
      backtrack(index+1, path)
      path.pop()
    
  backtrack(0, [])
  
  return results

print(letterCombinations("23"))