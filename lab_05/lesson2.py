import matplotlib as pit
import numpy as np 
import matplotlib.pyplot as plt
plt.title("пустое поле")
plt.plot()
plt.show()

plt.title("Линейный график, построенный по значениям y")
plt.plot([1, 7, 3, 5, 11, 1])
plt.show()

plt.title("Линейный график, построенный по значениям y и x")
plt.plot([1, 5, 10, 15, 20], [1, 7, 3, 5, 11])
plt.show()


x = [1, 5, 10, 15, 20]
y = [1, 7, 3, 5, 11]
plt.plot(x, y, label='steel price')
plt.title('Chart price', fontsize=15)
plt.xlabel('Day', fontsize=12, color='blue')
plt.ylabel('Price', fontsize=12, color='blue')
plt.legend()
plt.grid(True)
plt.text(15, 4, 'grow up!')
plt.show()

plt.title("Несколько графиков,с разными применёными стилями, построенные разными функциями plot()")
x = [1, 5, 10, 15, 20]
y1 = [1, 7, 3, 5, 11]
y2 = [i*1.2 + 1 for i in y1]
y3 = [i*1.2 + 1 for i in y2]
y4 = [i*1.2 + 1 for i in y3]
plt.plot(x, y1, '-', x, y2, '--', x, y3, '-.', x, y4, ':')
plt.show()

plt.title("изменение цвета линии")
x = [1, 5, 10, 15, 20]
y = [1, 7, 3, 5, 11]
plt.plot(x, y, '--r')
plt.show()


plt.plot(x, y1, 'ro')
plt.show()

plt.plot(x, y2, 'bx')
plt.show()


plt.subplot(2, 2, 1)
plt.plot(x, y1, '-')
plt.subplot(2, 2, 2)
plt.plot(x, y2, '--')
plt.subplot(2, 2, 3)
plt.plot(x, y3, '-.')
plt.subplot(2, 2, 4)
plt.plot(x, y4, ':')
plt.show()


fig, axs = plt.subplots(2, 2, figsize=(12, 7))
axs[0, 0].plot(x, y1, '-')
axs[0, 1].plot(x, y2, '--')
axs[1, 0].plot(x, y3, '-.')
axs[1, 1].plot(x, y4, ':')
plt.show()