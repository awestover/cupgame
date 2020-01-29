
import numpy as np
import matplotlib.pyplot as plt
p = 100
n = p+1
ROUNDS = 1000

cups = [0 for i in range(n)]

for i in range(ROUNDS):
    #  new_fill_level = (sum(cups) + p)/n
    #  for j in range(n):
    #      if cups[j] > new_fill_level:
    #          print("bro water you thinking")
    #      cups[j] = new_fill_level
    for j in range(n):
        cups[j] += 1/n

    cups.sort(key= lambda x: -x)
    for j in range(p):
        cups[j] = max(0, cups[j]-1)

plt.bar(list(range(n)), cups)
print(cups)
plt.show()

