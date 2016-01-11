import random

'''
problem 3:
Write a program to simulate the roll of three dice a large number of times and keep track of the proportion of times that the sum is 9 and the proportion of times it is 10.
'''

def threeDice():
  number = input("Number of times to roll the dice:")
  sum9 = 0
  sum10 = 0
  for amount in range(number):
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    roll3 = random.randint(1, 6)
    rolls = list((roll1, roll2, roll3))
    if (sum(rolls) == 9):
      sum9 += 1
    elif (sum(rolls) == 10):
      sum10 += 1

  print "number of sum 9 turns: " + str(sum9)
  print "number of sum 10 turns: " + str(sum10)

threeDice()

#it appears the hypthesis that sums of 9 appear less often than 10 is inconclusive