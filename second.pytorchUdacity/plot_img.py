import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from skimage import io

#style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
plt.axis('off')
# "./data/KITTI/testing/image_2/"+("%06d.jpg" % iterat)
iterat = 0
path = ''
def animate(i):
    global path
    path = open('plik.txt','r').read()
    if path != '':
        ax1.clear()
        image = io.imread(path)
        ax1.imshow(image)
        plt.axis('off')

ani = animation.FuncAnimation(fig, animate, interval=40)
plt.show()

