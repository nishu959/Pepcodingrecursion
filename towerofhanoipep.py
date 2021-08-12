n = int(input())

s = int(input())
d = int(input())
h = int(input())


def solve(s, d, h, n):
 
  if(n==1):
    print(n,"[", s, " -> ", d, "]", sep="")
    return
  
  solve(s, h, d, n-1)
 
  print(n,"[", s, " -> ", d, "]", sep="")
  
  solve(h, d, s, n-1)
  return
 

solve(s, d, h, n)
