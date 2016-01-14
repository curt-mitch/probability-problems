import random

'''
  problem 5:
  Calculate f(n), the probability of at least one triple-six when three dice are rolled n times. Determine the smallest value of n necessary for a favorable bet that a triple-six will occur when three dice are rolled n times.
'''

def tripleSix():
  number = input("Number of times to roll the dice:")
  tripleSixRoll = 0
  for amount in range(number):
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    roll3 = random.randint(1, 6)
    if all(roll == 1 for roll in (roll1, roll2, roll3)):
      tripleSixRoll += 1
  print "Number of triple six rolls: " + str(tripleSixRoll)

tripleSix()
# it seems than 300 seems to be roughly a good number to guarantee at least one roll of 3 sixes.