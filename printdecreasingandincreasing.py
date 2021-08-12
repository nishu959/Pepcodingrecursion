#print increasing and decreasing

print("decreasing")
n =int(input())

def fun1(n):
  if(n==0):
    return 0
  
  print(n) 
  fun1(n-1)
  

fun1(n)

print("increasing")
def fun2(n):
  if(n==0):
    return 0
   
  fun2(n-1)
  print(n)


fun2(n)

