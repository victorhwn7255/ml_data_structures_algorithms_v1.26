def letterCombinations(digits: str):
  NUM_TO_DIGIT = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
  }
  results = []
  
  def backtrack(index, path: list):
    if index == len(digits):
      results.append(''.join(path))
      return
    
    for char in NUM_TO_DIGIT[digits[index]]:
      path.append(char)
      backtrack(index + 1, path)
      path.pop()
      
  backtrack(0, [])
  return results

print(letterCombinations("23"))