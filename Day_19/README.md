# Day 19 : break and continue

## break statement

The break statement enables a program to skip over a part of the code. A break statement terminates the very loop it lies within.

**example:**

```
for i in range(1,101,1):
    print(i ,end=" ")
    if(i==50):
        break
    else:
        print("Mississippi")
print("Thank you")
```

output
```
1 Mississippi
2 Mississippi
3 Mississippi
4 Mississippi
5 Mississippi
.
.
.
50 Thank you
```

## continue statement

The continue keyword is used to end the current iteration in a for loop (or a while loop), and continues to the next iteration.


**example:**

```
for i in range(12):
  if(i == 10):
    print("Skip the iteration")
    continue
  print("5 X", i, "=", 5 * i)
```
  
output
  
```
5 X 0 = 0
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
Skip the iteration
5 X 11 = 55
```

## Day 19 Completed✅ 

* [Repl Link](https://replit.com/@kishanrajput23/19-Day-19-break-and-continue)

* [Tweet Link](https://twitter.com/kishan_rajput23/status/1603783426985058306?s=20&t=fH4Y-ZvF35YX8D-7MT3f8Q)
