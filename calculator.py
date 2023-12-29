a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
c = input("which operation to perform ??")
if(c == '+'):
    print("a+b = " , a+b)
elif(c == '-'):
    print("a-b = " , a-b)
elif(c == '*'):
    print("a*b = " , a*b)
elif(c == '/'):
    print("a/b = " , a/b)
elif(c == '**'):
    print("a**b = " , a**b)
elif(c == '//'):
    print("a//b = " , a//b)
else:
    print("enter valid operation")