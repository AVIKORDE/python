range=int(input("Enter range for Armstrong nos"))
no=1
while no<=range:
    n=no
    sum=0
    while n>0:
        rem=n%10
        n=int(n/10)
        sum=sum+rem**3
    if no==sum:
        print("Armstrong no=",str(no))
    no+=1    
print("===========================================")
