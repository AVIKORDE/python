   
def add(n1,n2):
    n3=n1+n2
    return (n3)
def sub(n1,n2):
    n3=n1-n2
    return (n3)
def mul (n1,n2):
    n3=n1*n2
    return (n3)
def div(n1,n2):
    n3=n1/n2
    return (n3)
choice=input("which oprator you want? choice:\n1 add\n2 sub\n3 mul\n4 div\n")
n1=int(input("enter first number"))
n2=int(input("enter second number"))
if (choice == 1):
    print(n1, "+", n2, add(n1,n2))
elif (choice == 2):
    print(n1, "-", n2, sub(n1,n2))
elif (choice == 3):
    print(n1, "*", n2, mul(n1,n2))
else:
    print(n1, "/", n2, div(n1,n2))


    
