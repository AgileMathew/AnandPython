def group(lists,size):
  result, temp = [], []
  count = 1
  for i in range(0,len(lists)):
    if count==size:
      temp.append(lists[i])
      result.append(temp)
      count=1
      temp = []
    else:
      temp.append(lists[i])
      count+=1

  if temp != []:
    result.append(temp)
  return result

print group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)

print group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4)

print group([1, 2, 3, 4, 5, 6, 7, 8, 9], 2)
