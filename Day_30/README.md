# Day 30 : Recursion

## Recursion in python
Recursion is the process of defining something in terms of itself.

### Python Recursive Function
In Python, we know that a function can call other functions. It is even possible for the function to call itself. These types of construct are termed as recursive functions.

**Example:**
```
def factorial(num): 
    if (num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num - 1)) 
  
# Driver Code 
num = 7; 
print("Number: ",num)
print("Factorial: ",factorial(num))
```

Output:
```
number:  7
Factorial:  5040
```

## Day 30 Completed✅ 

* [Repl Link](https://replit.com/@kishanrajput23/30-Day30-Recursion)

* [Tweet Link](https://twitter.com/kishan_rajput23/status/1607799327984070656?s=20&t=VWYD_Vh8k_93Num-BN0fjQ)
