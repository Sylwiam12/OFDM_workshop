# base
import matplotlib.pyplot as plt

x = [1,3, 6, 7]
y = [1,9,36,49]

plt.plot(x, y, '-p')
plt.grid()
plt.xlabel('V')
plt.ylabel('W')
plt.show()

# with building y
# import matplotlib.pyplot as plt

# x = [1,3, 6, 7]

# y = list()
# for i in x:
#     y.append(i*i)

# plt.plot(x, y, '-p')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.grid()
# plt.show()
