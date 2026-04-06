i=0
while(True):
    if i+1<5:
        i=i+1
        continue
    print(i+1, end=" ")
    if (i==44):
        break
    i=i+1


while(1):
    print("please enter your number\n")
    int2=int(input())
    if(int2<100):
        print("try again something")
        continue
    else:
        print("congratulations you entered correct number")
        break
