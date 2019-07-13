num1,q=map(int,input().split())
val=0
i=0
if num1<=100000:
  
  arrval=list(map(int,input().split()[:num1]))
  while(i<q):
    u,v=map(int,input().split())
    for j in range(u-1,v):
      val+=arrval[j]
    print(val)
    val=0
    i+=1
