for row in range(129):
    if row%2 ==0:
        for column in range(1,130):
            if column%2 ==1:
                if column !=129:
                    print(" ",end="")
                else:
                    print(" ")
            else:
                print("|",end="")
    else:
        print("--------------------------------------------------------------------------------------------------------------------------------")
if row==128 and column==129:
    print(True)
else:
    print(False)