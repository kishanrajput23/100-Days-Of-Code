import random, time, os

ques = [
  "The International Literacy Day is observed on?",
  "The language of Lakshadweep. a Union Territory of India, is",
  "In which group of places the Kumbha Mela is held every twelve years?",
  "Bahubali festival is related to?",
  "Which day is observed as the World Standards Day",
  "Which of the following was the theme of the World Red Cross and Red Crescent Day?",
  "September 27 is celebrated every year as",
  "Who is the author of 'Manas Ka-Hans'",
  "The death anniversary of which of the following leaders is observed as Martyrs Day?",
  "Who is the author of the epic 'Meghdoot'?"
]
opt = [
  "\nA.Sep 8 \nB.Nov 28 \nC.May 2 \nD.Sep 22",
  "A.Tamil \nB.Hindi \nC.Malayalam \nD.Telugu",
  "\nA.Ujjain. Purl; Prayag. Haridwar \nB.Prayag. Haridwar, Ujjain,Nasik \nC.Rameshwaram. Purl, Badrinath. Dwarika\nD.	Chittakoot, Ujjain, Prayag,'Haridwar",
  "\nA.Islam\nB.Hinduism\nC.Buddhism\nD.Jainism",
  "\nA.June 26\nB.Oct 14\nC.Nov 15\nD.Dec 2",
  "\nA.Dignity for all - focus on women\nB.Dignity for all - focus on Children'\nC.Focus on health for all\nD.Nourishment for all-focus on children",
  "\nA.Teachers Day\nB.National Integration Day\nC.World Tourism Day\nD.International Literacy Day",
  "\nA.Khushwant Singh\nB.Prem Chand\nC.Jayashankar Prasad\nD.Amrit Lal Nagar",
  "\nA.Smt. Indira Gandhi\nB.PI. Jawaharlal Nehru\nC.Mahatma Gandhi\nD.Lal Bahadur Shastri",
  "\nA.Vishakadatta\nB.Valmiki\nC.Banabhatta\nD.Kalidas"
]
ans = ["A", "C", "B", "D", "B", "B", "C", "D", "C", "D"]
key = [
  "A.Sep 8", "C.Malayalam", "B.Prayag. Haridwar, Ujjain,. Nasik", "D.Jainism",
  "B.Oct 14", "B.Dignity for all - focus on Children", "C.World Tourism Day",
  "D.Amrit Lal Nagar", "C.Mahatma Gandhi", "D.Kalidas"
]
quesasked = []
correctAnswer = 0
prize = 0
num = 1
while True:
  i = random.randint(0, (len(ques) - 1))
  if i not in quesasked:
    quesasked.append(i)
  else:
    continue
  print("KAUN BANEGA CROREPATI")
  print()
  print(num, ".", ques[i])
  num += 1
  print(opt[i])
  g = input("Enter the option\n >> ").strip().upper()
  if g == ans[i]:
    correctAnswer += 1
    if correctAnswer == 1:
      prize = 5000
    elif correctAnswer > 1:
      prize = prize * 2
    print("No. of Correct answers \n", correctAnswer)
    print("Money won ₹", prize)
    if (len(quesasked) == len(ques)):
      break
    else:
      time.sleep(2)
      os.system("clear")
      continue
  # elif g!="A" or g!="B" or g!="C" or g!="D":
  #   print("Invalid Choice. Try Again")

  else:
    print("Wrong Answer! You Lost")
    print("No. of Correct answers ", correctAnswer)
    print("Correct Answer was:", key[i])
    break

print("You won ₹", prize, "\nThanks for playing")
