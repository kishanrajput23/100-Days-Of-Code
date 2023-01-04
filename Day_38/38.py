a = int(input("Enter any value between 5 and 9 : "))

if(a<5  or a>9):
  raise  ValueError("Value should be between 5 and 9")
  
salary = int(input("Enter salary amount: "))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")
