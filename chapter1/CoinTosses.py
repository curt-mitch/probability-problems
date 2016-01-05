import random

#problem 1
def coinTosses():
  number = input("Number of times to flip the coin:")
  recordCount = { "T": 0, "H": 0 }
  heads = 0
  tails = 0
  for amount in range(number):
    flip = random.randint(0, 1)
    if (flip == 0):
      recordCount["T"] += 1
    else:
      recordCount["H"] += 1
    if (amount and amount % 100 == 0):
      print "proportion of heads: " + str(1.0 * recordCount["T"] / amount - 0.5)

coinTosses()
# the proportion of heads tosses does not appear to approach zero consistently