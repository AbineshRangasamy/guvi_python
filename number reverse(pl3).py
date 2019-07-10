n1=int(input())
t1=n1
rev1=0
while(n1>0):
    dig=n1%10
    rev1=rev1*10+dig
    n1=n1//10
print(rev1)
