
N=int(input("Enter the value of N:"))
a=0
b=1
sum=0
count=1
print("Fibonacci Series:")
while(count<=N):
  print(sum)
  count+=1
  a=b
  b=sum
  sum=a+b