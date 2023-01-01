# Day 35 : For Loop With Else

## Python - else in Loop
As you have learned before, the else clause is used along with the if statement.

Python allows the else keyword to be used with the for and while loops too. The else block appears after the body of the loop. The statements in the else block will be executed after all iterations are completed. The program exits the loop only after the else block is executed.

**Syntax:**
```
for counter in sequence:
    #Statements inside for loop block
else:
    #Statements inside else block
```

**Example:**
```
for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")
```

**Output:**
```
iteration no 1 in for loop
iteration no 2 in for loop
iteration no 3 in for loop
iteration no 4 in for loop
iteration no 5 in for loop
else block in loop
Out of loop
```

## Day 35 Completed✅ 

* [Repl Link](https://replit.com/@kishanrajput23/35-Day-35-For-loop-with-else)

* [Tweet Link](https://twitter.com/kishan_rajput23/status/1609535573102071810?s=20&t=c0btCyx11upWUh4zl753Bg)
