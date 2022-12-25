# Day 28 : f strings

## String formatting in python
String formatting can be done in python using the format method.
```
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
```

Output:
```
For only 49.10 dollars!
```

## f-strings in python
It is a new string formatting mechanism introduced by the PEP 498. It is also known as Literal String Interpolation or more commonly as F-strings (f character preceding the string literal). The primary focus of this mechanism is to make the interpolation easier.

When we prefix the string with the letter 'f', the string becomes the f-string itself. The f-string can be formatted in much same as the str.format() method. The f-string offers a convenient way to embed Python expression inside string literals for formatting.

**Example**
```
val = 'Geeks'  
print(f"{val}for{val} is a portal for {val}.")  

name = 'Tushar'  
age = 23  
print(f"Hello, My name is {name} and I'm {age} years old.")
```

Output:
```
GeeksforGeeks is a portal for Geeks.

Hello, My name is Tushar and I'm 23 years old.
```
In the above code, we have used the f-string to format the string. It evaluates at runtime; we can put all valid Python expressions in them.

We can use it in a single statement as well.

**Example**
```
print(f"{2 * 30})"
```

Output:
```
60
```

## Day 28 Completed✅ 

* [Repl Link](https://replit.com/@kishanrajput23/28-Day28-f-strings)

* [Tweet Link](https://twitter.com/kishan_rajput23/status/1607077227304472578?s=20&t=qGpedt1YnMoCrZw3d-y0EQ)
