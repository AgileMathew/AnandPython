def unique(x,key):
  result = []
  for i in x:
    i = key(i)
    if i not in result:
      result.append(i)
  return result

print unique(["python","java","WOO","Python","Java"],key=lambda s : s.lower())
