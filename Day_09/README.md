# Day 9 : Typecasting in python

The conversion of one data type into the other data type is known as type casting in python or type conversion in python.

Python supports a wide variety of functions or methods like: int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict(), etc. for the type casting in python.

## Two Types of Typecasting:

* Explicit Conversion (Explicit type casting in python)
* Implicit Conversion (Implicit type casting in python).

## Explicit typecasting:
The conversion of one data type into another data type, done via developer or programmer's intervention or manually as per the requirement, is known as explicit type conversion.

It can be achieved with the help of Python’s built-in type conversion functions such as int(), float(), hex(), oct(), str(), etc .

**Example of explicit typecasting:**

```
string = "15"
number = 7
string_number = int(string) #throws an error if the string is not a valid integer
sum = number + string_number
print("The Sum of both the numbers is: ", sum)
```
Output:
```
The Sum of both the numbers is 22
```

## Implicit typecasting:

Data types in Python do not have the same level i.e. ordering of data types is not the same in Python. Some of the data types have higher-order, and some have lower order. 

While performing any operations on variables with different data types in Python, one of the variable's data types will be changed to the higher data type. 

According to the level, one data type is converted into other by the Python interpreter itself (automatically). This is called, implicit typecasting in python. Python converts a smaller data type to a higher data type to prevent data loss.

**Example of implicit typecasting:**
```
# Python automatically converts
# a to int
a = 7
print(type(a))
 
# Python automatically converts b to float
b = 3.0
print(type(b))
 
# Python automatically converts c to float as it is a float addition
c = a + b
print(c)
print(type(c))
```

Ouput:
```
<class 'int'>
<class 'float'>
10.0
<class 'float'>
```

## Day 9 Completed✅ 

* [Repl Link](https://replit.com/@kishanrajput23/09-Day9-Typecasting-in-Python)

* [Tweet Link](https://twitter.com/kishan_rajput23/status/1600171036141842433?s=20&t=9m-s4Cm2kl3l66tPOR_9aA)
