import numpy as np
import matplotlib.pyplot as plt


class particle:
    '''
    粒子坐标为list，存储所有圈数中的数据
    tag为整数，因为tag不会改变
    '''
    def __init__(self, i, Np):
        self.x = []
        self.px = []
        self.y = []
        self.py = []
        self.z = []
        self.pz = []

        self.tag = i
        # 粒子初始位置，单位是相应方向的sigma
        self.x0 = i // (int(np.sqrt(Np)))
        self.y0 = i % (int(np.sqrt(Np)))

    def print(self):
        print("\nparticle[%d], (x0, y0) = (%f, %f)" %
              (self.tag, self.x0, self.y0))
        for i in range(0, len(self.x)):
            print(
                "order%d: x = %e, px = %e, y = %e, py = %e, z = %e, pz = %e" %
                (i, self.x[i], self.px[i], self.y[i], self.py[i], self.z[i],
                 self.pz[i]))

    def fft(self):
        self.sp_x = np.abs(np.fft.fft(np.array(self.x)))
        self.sp_y = np.abs(np.fft.fft(np.array(self.y)))
        self.freq_x = np.abs(np.fft.fftfreq(len(self.x)))
        self.freq_y = np.abs(np.fft.fftfreq(len(self.y)))

        self.tunex = find_mode(self.sp_x, self.freq_x)
        self.tuney = find_mode(self.sp_y, self.freq_y)


class tuneline:
    '''
    保存粒子tune值
    '''
    def __init__(self, data, order):
        self.footx_x = []
        self.footx_y = []
        self.footy_x = []
        self.footy_y = []
        for i in range(0, len(data)):
            if data[i].x0 == order:
                self.footx_x.append(data[i].tunex)
                self.footx_y.append(data[i].tuney)
            if data[i].y0 == order:
                self.footy_x.append(data[i].tunex)
                self.footy_y.append(data[i].tuney)


def find_mode(spectrum, freq):
    max_freq = 0
    max_amplitude = 0
    for i in range(freq.shape[0]):
        if spectrum[i] > max_amplitude:
            max_amplitude = spectrum[i]
            max_freq = freq[i]
    return max_freq


def load_partilce(file, data, Np):
    x, px, y, py, z, pz, tag = np.loadtxt(
        file,
        delimiter=",",
        skiprows=1,
        usecols=(0, 1, 2, 3, 4, 5, 6),
        unpack=True,
    )

    # 判断读取的文件中粒子数是否与输入参数相同
    if Np != (np.size(x)):
        print("Error: Np is not equal to file size, Np = %d, file size = %d" %
              (Np, np.size(x)))

    # 把numpy.float64类型转化为int类型
    tag = tag.astype(int)

    for i in range(0, Np, 1):
        order = tag[i]
        data[order].x.append(x[i])
        data[order].px.append(px[i])
        data[order].y.append(y[i])
        data[order].py.append(py[i])
        data[order].z.append(z[i])
        data[order].pz.append(pz[i])
        data[order].tag = tag[i]


if __name__ == "__main__":

    # 文件路径及相关参数
    dir1 = "E:\\changmx\\bb2021\\distribution"
    dir2 = "\\2021_0409"
    dir3 = "\\2029_27_"
    dir4 = "proton"

    nturn = 10000
    Np = 49
    bunch = 0

    # 创建保存粒子的列表，列表元素个数为粒子数，初始化粒子的tag信息
    data = []
    for i in range(0, Np):
        data.append(particle(i, Np))
        data[i].print()

    # 读取nturn圈数个文件中的粒子信息
    for turn in range(0, nturn):
        file = (dir1 + dir2 + dir3 + dir4 + "_turn" + str(turn) + "_bunch" +
                str(bunch) + "_" + str(Np) + ".csv")
        load_partilce(file, data, Np)

    for i in range(0, Np):
        data[i].fft()
        const = int(np.sqrt(Np))
        print("x0 = %d, y0 = %d, tune x = %.5f, tune y = %.5f" %
              (data[i].x0, data[i].y0, data[i].tunex, data[i].tuney))

    # data[2].print()
    # print(data[2].x)

    fig, ax = plt.subplots()
    # for i in range(0, Np):
        # ax.scatter(data[i].tunex, data[i].tuney)
    # ax.plot(data[10].freq_x,data[10].sp_x)

    for i in range(0, int(np.sqrt(Np))):
        line = tuneline(data, i)
        ax.plot(
            line.footx_x,
            line.footx_y,
            label=str(i) + "$ sigma_x$",
        )
        ax.plot(
            line.footy_x,
            line.footy_y,
            label=str(i) + "$ sigma_y$",
        )

    ax.grid()
    ax.legend()
    plt.show()