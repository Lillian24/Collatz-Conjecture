x=int(input("enter the values:"))
n=0
count=0
while(n!=1):
    if(x%2==0):
        n=x/2
        print(int(n))
        x=n
        count+=1
    else:
        n=(3*x)+1
        print(int(n))
        x=n
        count+=1
print("steps taken to approach the 4,2,1 loop:",count)
    