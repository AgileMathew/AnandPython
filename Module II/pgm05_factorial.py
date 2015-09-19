#Problem 5: Write a function factorial to compute factorial of a number. Can you use the product function defined in the previous example to compute factorial?


def fact(n):
  prod=1
  if(n==0):
    print "factorial is"
  elif (n<0):
      print "factorial doesnot exit"
  else:
    for i in range(1,n+1):
      prod = prod * i
  return prod

print fact(4)
