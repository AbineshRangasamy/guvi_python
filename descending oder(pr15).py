num=int(input())
if num<10000:
  arr=list(map(int,input().split()))
  arr.sort(reverse=True)
  for i in arr:
    print(i)