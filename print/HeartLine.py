import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    x = np.linspace(-8, 8, 1024)
    y1 = 0.618 * np.abs(x) - 0.8 * np.sqrt(64 - x ** 2)
    y2 = 0.618 * np.abs(x) + 0.8 * np.sqrt(64 - x ** 2)
    plt.plot(x, y1, color='r')
    plt.plot(x, y2, color='r')
    print(x, y1, y2)
    # # FuncAnimation会在每一帧都调用update函数
    # # 在这里设置一个10帧的动画，每帧之间间隔200ms
    # anim = animation.FuncAnimation(plt.plot, update, frames=np.arange(0, 10), interval=200)  # frame:帧
    # # 我知道问什么这里提示figundefine了，因为前面的fig在函数中声明的
    plt.show()
