import matplotlib.pyplot as plt

x = [0, 1, 2, 3]
y = [5, 10, 15, 20]

plt.step(x, y, where='mid')  # 'mid' can be 'pre' or 'post'
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Step Curve Example')
plt.show()
