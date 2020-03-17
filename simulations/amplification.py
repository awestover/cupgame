import numpy as np
import matplotlib.pyplot as plt

#  def f(m,k):
#      if m==1:
#          if k >= 1:
#              return np.log2(k)
#          else:
#              return 0
#      else:
#          s = 0
#          while k > 0:
#              s += f(m-1,k)
#              k>>=1
#          return s

def f(m,k):
    s = 0
    vals = [k]
    for i in range(m):
        new_vals = []
        for val in vals:
            j = 1
            while val>>j > 1:
                new_vals.append(val>>j)
                j += 1
        vals = new_vals
    #  print(vals)
    #  return 0.5*sum([max(np.log2(val), 0) for val in vals])
    return vals

x = f(3, 1<<9)
unique = list(set(x))
unique.sort()
for i in unique:
    print(f"count({i}) = {x.count(i)}")

#  datapts = [2**i for i in range(2,20)]
#  datapts = [1024*i for i in range(1,128)]
#  simulated = [f(int(np.log(n))+2, n) for n in datapts]
#  conjectured = [n**0.582 for n in datapts]
#  plt.plot(datapts, conjectured)
#  plt.plot(datapts, simulated)
#  plt.show()


# um this isnt working so well
