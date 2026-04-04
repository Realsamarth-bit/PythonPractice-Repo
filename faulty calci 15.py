while True:
    print("inpput enter first number")
    i1=int(input())
    print("input your number")
    i2=int(input())
    print("enter your expression ")
    op=input()
    break

if op=='+':
    if i1==56 and i2==9:
        print("77")
    else:
        print(i1+i2)
elif op=='-':
        print(i1-i2)
elif op=='*':
    if i1==45 and i2==3:
        print("555")
    else:
        print(i1*i2)
elif op=='/':
    if i1==56 and i2==6:
        print("4")
    else:
        print(i1/i2)
else:
    print("invalid expression or number")
    print("_------------------")
    print("---------------")

