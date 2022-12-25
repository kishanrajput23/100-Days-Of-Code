letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Harry"

val = 'Geeks'  
print(f"{val}for{val} is a portal for {val}.")  

name = 'Tushar'  
age = 23  
print(f"Hello, My name is {name} and I'm {age} years old.")

print(letter.format(country, name))
print(f"Hey my name is {name} and I am from {country}")
print(f"We use f-strings like this: Hey my name is {name} and I am from {country}")

price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)
print(txt.format())
print(type(f"{2 * 30}"))
