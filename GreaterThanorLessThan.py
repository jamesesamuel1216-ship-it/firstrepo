num1str=input("enter number 1 here: ")
num2str=input("enter number 2 here: ")

num1=float(num1str)
num2=float(num2str)

def sub(num1,num2):
    value=num1-num2
    return value

if sub(num1,num2) < 0:
    print(f"Number 1 is Less than Number 2 by {abs(sub(num1,num2))}")
elif sub(num1,num2) == 0:
    print("Number 1 is the same as Number 2")
else:
    print(f"Number 1 is greater than Number 2 by {sub(num1,num2)}")
