import matplotlib as pit
import numpy as np 
import matplotlib.pyplot as plt
import math

#первый вариант легенды
x = [1, 5, 10, 15, 20]
y1 = [1, 7, 3, 5, 11]
y2 = [4, 3, 1, 8, 12]
plt.title("первый вариант легенды")
plt.plot(x, y1, 'o-r', label='line 1')
plt.plot(x, y2, 'o-.g', label='line 1')
plt.legend()
plt.show()


#второй варинт легенды
plt.title("второй вариант легенды")
plt.plot(x, y1, 'o-r')
plt.plot(x, y2, 'o-.g')
plt.legend(['L1', 'L2'])
plt.show()

#третий вариант легенды
plt.title("третий вариант легенды")
line1, = plt.plot(x, y1, 'o-b')
line2, = plt.plot(x, y2, 'o-.m')
plt.legend((line2, line1), ['L2', 'L1'])
plt.show()

#"постановки легенды при помощи loc"
locs = ['best', 'upper right', 'upper left', 'lower left',
'lower right', 'right', 'center left', 'center right',
'lower center', 'upper center', 'center']
plt.figure(figsize=(12, 12))

for i in range(3):
    for j in range(4):
        if i*4+j < 11:
            plt.subplot(3, 4, i*4+j+1)
            plt.title(locs[i*4+j])
            plt.plot(x, y1, 'o-r', label='line 1')
            plt.plot(x, y2, 'o-.g', label='line 2')
            plt.legend(loc=locs[i*4+j])
        else:
            break
plt.show()

plt.title("настройка внешнего вида легенды")
plt.plot(x, y1, 'o-r', label='line 1')
plt.plot(x, y2, 'o-.g', label='line 1')
plt.legend(fontsize=14, shadow=True, framealpha=1, facecolor='y',
edgecolor='r', title='Легенда')
plt.show()

x1 = [1, 2, 3, 4, 5]
y3 = [9, 4, 2, 4, 9]
y4 = [1, 7, 6, 3, 5]
y5 = [-7, -4, 2, -4, -7]
fg = plt.figure(figsize=(9, 4), constrained_layout=True)
gs = fg.add_gridspec(2, 2)
fig_ax_1 = fg.add_subplot(gs[0, :])
plt.plot(x1, y4)
plt.title("свободная компановка графика")
fig_ax_2 = fg.add_subplot(gs[1, 0])
plt.plot(x1, y3)
fig_ax_3 = fg.add_subplot(gs[1, 1])
plt.plot(x1, y5)
plt.show()

x = [i for i in range(10)]
y = [i*2 for i in range(10)]
plt.title("подпись осей")
plt.plot(x, y)
plt.xlabel('Ось X\nНезависимая величина', fontsize=14, fontweight='bold')
plt.ylabel('Ось Y\nЗависимая величина', fontsize=14, fontweight='bold')
plt.show()

bbox_properties=dict(boxstyle='darrow, pad=0.3', ec='k', fc='y', ls='-',
lw=3)
plt.text(2, 7, 'HELLO!', fontsize=15, bbox=bbox_properties)
plt.plot(range(0,10), range(0,10))
plt.title("текстовый блок")
plt.show()

x = list(range(-5, 6))
y = [i**2 for i in x]
plt.annotate('min', xy=(0, 0), xycoords='data', xytext=(0, 10),
textcoords='data', arrowprops=dict(facecolor='g'))
plt.plot(x, y)
plt.title("анотации")
plt.show()

from mpl_toolkits.axes_grid1.inset_locator import inset_axes
np.random.seed(123)
vals = np.random.randint(11, size=(7, 7))
fig, ax = plt.subplots()
gr = ax.pcolor(vals)
plt.title("Colorbar с собственной шкалой")
axins = inset_axes(ax, width="7%", height="50%", loc='lower left',
bbox_to_anchor=(1.05, 0., 1, 1), bbox_transform=ax.transAxes,
borderpad=0)
plt.colorbar(gr, cax=axins)
cbar = plt.colorbar(gr, cax=axins, ticks=[0, 5, 10], label='Value')
cbar.ax.set_yticklabels(['Low', 'Medium', 'High'])
plt.show()

