num=input()
lu=list(map(int,input().split()))
lu = [bin(xl) for xl in lu]
lu.sort(reverse=True)
lu = [int(x,2) for x in lu]
for xl in lu:
  print(xl)
