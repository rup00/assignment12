
N=int(input("Enter the value of N: "))
count=0
i=2

while(count<N):
    j=2
    flag=0
    while(j<=i//2):
        if(i%j==0):
            flag=1
            break
        j=j+1
    if(flag==0):
        print(i,end=" ")
        count=count+1
    i=i+1