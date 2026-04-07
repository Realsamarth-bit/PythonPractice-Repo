num=18
print("enter a number to guess")

while(True):
    numberofguess=32
    input1=int(input())
    if input1<18:
        print("guess upper number")
        print("number of guess left",numberofguess-1)
        numberofguess=31
        if numberofguess==0:
            print("you lost")
            break
        else:
            continue
    elif input1>18:
        print("guess lower number")
        continue
    else:
        print("number is correct")
        break

        #samarth bandekar
        #samarthbandekar_
        #instagram