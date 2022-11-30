n=int(input())
add=0
product=1
while n!=0:
    rem=n%10
    n=n//10
    add=add+rem
    product=product*rem
result=product-add
print(result)
