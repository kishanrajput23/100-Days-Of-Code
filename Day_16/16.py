x = int(input("Enter the value of x: "))
# x is the variable to match\

match x:
    # if x is 0
    case 0:
        print("x is zero")
      
    # case with if-condition
    case 4:
        print("case is 4")

    case _ if x<0:
        print(x, "is negative number")
    case _ if x>100:
        print(x, "is greater then 100")
    case _:
        print("Your number is", x)
