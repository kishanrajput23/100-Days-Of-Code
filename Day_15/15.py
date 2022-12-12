import time
# https://docs.python.org/3/library/time.html#time.strftime

print("===== Welcome Sir =====")
name = input("Please enter your name : ")

timestamp = int(time.strftime('%H'))
print(timestamp)

if timestamp >=1 and timestamp <= 11:
  print("Good Morning",name, "Sir")

elif timestamp >= 12 and timestamp <= 15:
  print("Good Afternoon",name, "Sir")

elif timestamp >= 16 and timestamp <= 20:
  print("Good Evening",name, "Sir")

elif timestamp >= 21 and timestamp <= 24:
  print("Good Evening",name, "Sir")

else:
  print("You're not living on Earth.")
