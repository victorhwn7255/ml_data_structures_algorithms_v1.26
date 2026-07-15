def increasingTriplet(nums:list[int]):
  first_num = float("inf")
  second_num = float("inf")
  
  for num in nums:
    if num <= first_num:
      first_num = num
    elif num <= second_num:
      second_num = num
    else:
      return True
  
  return False