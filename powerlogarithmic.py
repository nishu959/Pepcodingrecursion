n =int(input())
p = int(input())

def fun1(n, p):
  if(p==0):
    return 1
  
  if(p%2==0):
    ans = fun1(n, p//2) * fun1(n, p//2) 
    return ans
  
  else:
    ans = n * fun1(n,p//2) * fun1(n, p//2)
    return ans
  

print(fun1(n, p)) 

