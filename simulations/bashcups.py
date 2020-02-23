
import matplotlib.pyplot as plt

n = 1000
p = n-1
cups = [{"fill": 0, "id": i} for i in range(n)]

past_avgfills = []

for itter in range(100):
    keep_up_set = []
    for i in range(p):
        # filler
        standard_fill = (p-len(keep_up_set)) / (n-len(keep_up_set)) # len(keep_up_set) is approx i
        for j in range(n):
            if cups[j]["id"] in keep_up_set:
                cups[j]["fill"] += 1
            else:
                cups[j]["fill"] += standard_fill

        # (greedy) emptier
        cups.sort(key=lambda x: -x["fill"])
        for j in range(p):
            cups[j]["fill"] = max(cups[j]["fill"] -1, 0)

        for j in range(p, n):
            # concern: what if j is already in keep_up_set???
            # solution: well, that'd probably be good...
            if cups[j]["id"] not in keep_up_set:
                keep_up_set.append(cups[j]["id"]) 
        
        cups.sort(key=lambda x: -x["fill"])

        if i % (p//10) == 0:
            past_avgfills.append(sum([x["fill"] for x in cups])/n)
            plt.plot(past_avgfills)
            #  plt.stem([x["fill"] for x in cups])
            plt.pause(0.01)
            plt.cla()

