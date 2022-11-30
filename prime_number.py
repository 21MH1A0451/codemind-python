num=int(input())
for i in range(2,num):
    if (num%i)==0:
        break
if(i+1==num):
    print("prime")
else:
    print("not a prime")