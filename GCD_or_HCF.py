def gcd(a,b):
    if b==0:
        return a
    if a>b:
        a,b=b,a
    return gcd(a,b%a)
a,b=map(int,input().split())
print(gcd(a,b))