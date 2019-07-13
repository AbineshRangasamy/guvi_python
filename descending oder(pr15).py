num=int(input())
if num<10000:
  arr=list(map(int,input().split()))[:num]
  arr1=[]
  for r in arr:
    ab=bin(r)
    arr1.append(ab)
  arr.sort(reverse=True)
  for i in arr:
    print(i)
