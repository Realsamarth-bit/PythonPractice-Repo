num=18
print("enter a number to guess")
numberofguess=12


while(True):
    input1=int(input())
    if input1<18:
        print("guess upper number")
        numberofguess-=1
        print(numberofguess)
    elif input1>18:
        print("guess lower number")
        continue
    else:
        print("number is correct")
        if numberofguess==0:
            print("ypu lost")
            break

        #samarth bandekar
        #samarthbandekar_
        #instagram