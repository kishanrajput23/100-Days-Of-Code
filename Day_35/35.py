i = 0
while i<7:
  print(i)
  i = i + 1
  # if i == 4:
  #   break

else:
  print("Sorry no i")

for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")

for i in range(0, 4):
  print(i)
  if i == 2:
    break
    
else: # Not executed as there is a break
	print("No Break")
