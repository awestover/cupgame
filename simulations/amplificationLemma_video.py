
import numpy as np
import matplotlib.pyplot as plt

n=200
cups = np.random.rand(n)*3-1.5 # fillls
cups.sort()

delta = 1/4

# note: these are for the current level of recursion
A = [] # indexes into cups
B = [] # indexes into cups

sorted_cups_idxs = np.argsort(cups)
a = int(delta * n)
A = sorted_cups_idxs[0:a]
B = sorted_cups_idxs[a:n]
p=a+1

for idx in range(a):
    # single processor cup game
    un_neglected = B[:]
    while len(un_neglected) > 1:
        # filler
        for jj in A:
            cups[jj] += 1
        for jj in un_neglected:
            cups[jj] += 1/len(un_neglected)

        # emptier 
        emptiers_idxs = np.argsort(cups)[-p:]
        for jj in emptiers_idxs:
            cups[jj] -= 1

        if len(un_neglected) % 100 == 0 or len(un_neglected) < 2:
            plt.ylim(-10,10)
            plt.bar([i for i in range(idx)], [cups[i] for i in A[:idx]], color="r")
            plt.bar([i for i in range(idx, a)], [cups[i] for i in A[idx:]], color="g")
            plt.bar([i for i in range(a, n)], [cups[i] for i in B], color="b")
            plt.pause(0.01)
            plt.cla()

        popped_it = False
        for j in range(len(un_neglected)):
            if un_neglected[j] in emptiers_idxs:
                un_neglected = np.delete(un_neglected, j)
                popped_it = True
                break

        if not popped_it:
            un_neglected = np.delete(un_neglected, np.random.randint(len(un_neglected)))

    # do the swap
    swap_cup = np.where(B==un_neglected[0])[0][0]
    if cups[A[idx]] < cups[B[swap_cup]]:
        A[idx], B[swap_cup] = B[swap_cup], A[idx]


# recurse

old_cups = B[:]
new_cups = A[:]
new_n = len(new_cups)

sorted_cups_idxs_blah = np.argsort([cups[i] for i in new_cups])
sorted_cups_idxs = np.array([new_cups[i] for i in sorted_cups_idxs_blah])
a = int(delta * new_n)
A = sorted_cups_idxs[0:a]
B = sorted_cups_idxs[a:new_n]
p=a+1


for idx in range(a):
    # single processor cup game
    un_neglected = B[:]
    while len(un_neglected) > 1:
        # filler
        for jj in A:
            cups[jj] += 1
        for jj in un_neglected:
            cups[jj] += 1/len(un_neglected)

        # emptier 
        emptiers_idxs = np.argsort(cups)[-p:]
        for jj in emptiers_idxs:
            cups[jj] -= 1

        if len(un_neglected) % 1 == 0 or len(un_neglected) < 15:
            plt.ylim(-10,10)
            plt.bar([i for i in range(idx)], [cups[i] for i in A[:idx]], color="r")
            plt.bar([i for i in range(idx, a)], [cups[i] for i in A[idx:]], color="g")
            plt.bar([i for i in range(a, new_n)], [cups[i] for i in B], color="b")

            plt.bar([i for i in range(new_n,n)], [cups[i] for i in old_cups], color="k")
            plt.pause(0.01)
            plt.cla()

        popped_it = False
        for j in range(len(un_neglected)):
            if un_neglected[j] in emptiers_idxs:
                un_neglected = np.delete(un_neglected, j)
                popped_it = True
                break

        if not popped_it:
            un_neglected = np.delete(un_neglected, np.random.randint(len(un_neglected)))

    # do the swap
    swap_cup = np.where(B==un_neglected[0])[0][0]
    if cups[A[idx]] < cups[B[swap_cup]]:
        A[idx], B[swap_cup] = B[swap_cup], A[idx]


