import random

'''
  In Las Vegas, a roulette wheel has 38 slots numbered 0, 00, 1, 2, . . . , 36. The 0 and 00 slots are green and half of the remaining 36 slots are red and half are black. A croupier spins the wheel and throws in an ivory ball. If you bet 1 dollar on red, you win 1 dollar if the ball stops in a red slot and otherwise you lose 1 dollar. Write a program to find the total winnings for a player who makes 1000 bets on red.
'''

def rouletteBet():
  winnings = 1000
  for amount in range(1, 1000):
    num = random.randint(1, 36)
    if (num % 2 == 0):
      winnings += 1
    else:
      winnings -= 1
  print "winnings: " + str(winnings)

rouletteBet()