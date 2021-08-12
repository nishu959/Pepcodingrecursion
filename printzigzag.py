n = int(input())

def fun(n):
  if(n==0):
    return 0
  
  print(n,end = " ") 
  fun(n-1)
  print(n, end = " ")
  fun(n-1)
  print(n, end = " ")
  
fun(n)
