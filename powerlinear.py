n =int(input())
p = int(input())

def fun1(n, p):
  if(p==0):
    return 1
  
  ans = n * fun1(n,p-1)
  return ans
  

print(fun1(n, p)) 

