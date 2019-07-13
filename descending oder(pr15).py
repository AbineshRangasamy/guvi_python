num1=int(input())
if num1<10000:
  arr2=list(map(int,input().split()))[:num]
  arr1=[]
  for r in arr2:
    ab=bin(r)
    arr1.append(ab)
  arr2.sort(reverse=True)
  for i in arr2:
    print(i)
