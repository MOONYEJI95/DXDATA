import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10,7))
plt.boxplot(([100,87,29,76,88],[20,30,20,10000,20]))
plt.grid()
plt.show()
fig.savefig("gragh.png")

