for row in range(67):
    if row%2 ==0:
        for column in range(1,68):
            if column%2 ==1:
                if column !=67:
                    print(" ",end="")
                else:
                    print(" ")
            else:
                print("|",end="")
    else:
        print("-------------------------------------------------------------------")
if row==66 and column==67:
    print(True)
else:
    print(False)