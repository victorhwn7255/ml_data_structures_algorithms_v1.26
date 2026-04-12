def generateParenthesis(n: int):
  results = []
  
  def backtrack(path: list, open_count, close_count):
    if len(path) == n*2:
      results.append(''.join(path))
      return
  
    if open_count < n:
      path.append("(")
      backtrack(path, open_count+1, close_count)
      path.pop()
      
    if close_count < open_count:
      path.append(")")
      backtrack(path, open_count, close_count+1)
      path.pop()
  
  backtrack([], 0, 0)
  
  return results

print(generateParenthesis(3))