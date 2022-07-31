import random
import matplotlib.pyplot as plt
x = range(60)
y_shanghai=[random.uniform(15,18) for i in x]

plt.figure(figsize=(20,8),dpi=80)

plt.plot(x,y_shanghai)
x_label = ["11:{}".format(i) for i in x]
plt.yticks(range(40)[::5])
plt.xticks(x[::5],x_label[::5])
plt.grid(True,linestyle="--",alpha=0.5)
plt.savefig("shanghai.jpg")
plt.show()



