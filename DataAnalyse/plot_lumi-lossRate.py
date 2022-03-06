from cProfile import label
from turtle import color
import numpy as np
import matplotlib.pyplot as plt


def get_lumi_loss(path,
                  rateList,
                  startRowIndex=0,
                  startRowCount=200,
                  endRowIndex=-1,
                  endRowCount=200,
                  skiprows=2):
    turn, lumi = np.loadtxt(path,
                            delimiter=',',
                            skiprows=skiprows,
                            usecols=(0, 1),
                            unpack=True)
    # print(lumi[0:startrows:1])
    # print(lumi[-1:-1 - endrows:-1])
    startLoss = np.mean(lumi[startRowIndex:startRowIndex + startRowCount:1])
    if endRowIndex == -1:
        endLoss = np.mean(lumi[endRowIndex:-1 - endRowCount:-1])
    else:
        endLoss = np.mean(lumi[endRowIndex:endRowIndex + endRowCount:1])
    lossRate = -1 * (endLoss - startLoss) / startLoss

    rateList.append(lossRate)
    print('rate: {0:.6f}, from file: {1:s}'.format(lossRate, path))


def plot_lumi_loss(x, y):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.grid()
    myfontsize = 15

    ax.plot(x, y, marker='^', ls='--', lw=1, ms=8)

    ax.set_yscale('log')
    ax.set_xlabel(r'Number of proton particles $(\mathrm{N_p/N_{p0}})$',
                  fontsize=myfontsize)
    ax.set_ylabel(r'Luminosity loss rate $(\mathrm{-(L-L_0)/L_0})$',
                  fontsize=myfontsize)
    plt.xticks(fontsize=myfontsize)
    plt.yticks(fontsize=myfontsize)

    # plt.savefig(
    #     r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\lumi loss rate.png',
    #     dpi=300)
    plt.show()


if __name__ == '__main__':
    path_1Ne_xNp = []
    rate_1Ne_xNp = []

    path_xNe_1Np = []
    rate_xNe_1Np = []

    path_1Ne_xNp_change_Qex = []
    rate_1Ne_xNp_change_Qex = []

    path_1Ne_xNp_change_Qpx = []
    rate_1Ne_xNp_change_Qpx = []

    path_1Ne_1Np_change_Np = []
    rate_1Ne_1Np_change_Np = []

    path_1Ne_1Np_change_Ne = []
    rate_1Ne_1Np_change_Ne = []

    path_1Ne_xNp_instability = []
    rate_1Ne_xNp_instability = []

    path_1Ne_1Np_instability = []
    rate_1Ne_1Np_instability = []

    ############################################################  4e-7p，质子流强极限

    path_1Ne_xNp.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-0.1Np-稳定-1603_49\1603_49_luminosity_electron_350000turns.csv'
    )
    path_1Ne_xNp.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-0.2Np-稳定-1939_00\1939_00_luminosity_electron_350000turns.csv'
    )
    path_1Ne_xNp.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-0.3Np-稳定-1937_19\1937_19_luminosity_electron_350000turns.csv'
    )
    path_1Ne_xNp.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-0.4Np-sp=20w-1004_39\1004_39_luminosity_electron_1400000turns.csv'
    )

    #####
    path_1Ne_xNp_instability.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-0.4Np-sp=20w-1004_39\1004_39_luminosity_electron_1400000turns.csv'
    )
    #####

    # path_1Ne_xNp.append(
    #     r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-0.4Np-sp=14w-1343_18\1343_18_luminosity_proton_800000turns.csv'
    # )
    # path_1Ne_xNp.append(
    #     r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-0.4Np-sp=10w-最后水平方向有轻微相干运动-1051_43\1051_43_luminosity_proton_400000turns.csv'
    # )
    path_1Ne_xNp.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-0.5Np-不稳定-1950_23\1950_23_luminosity_electron_350000turns.csv'
    )
    path_1Ne_xNp.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-0.6Np-不稳定-1729_35\1729_35_luminosity_electron_350000turns.csv'
    )
    path_1Ne_xNp.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-0.7Np-不稳定-1012_56\1012_56_luminosity_electron_350000turns.csv'
    )
    # path_1Ne_xNp.append(
    #     r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-0.8Np-不稳定-0915_43\0915_43_luminosity_electron_350000turns.csv'
    # )
    path_1Ne_xNp.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-0.8Np-不稳定-sp=10w-1112_29\1112_29_luminosity_electron_700000turns.csv'
    )

    # path_1Ne_xNp.append(
    #     r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-0.84Np-不稳定-1005_28\1005_28_luminosity_electron_350000turns.csv'
    # )
    # path_1Ne_xNp.append(
    #     r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-0.88Np-不稳定-2300_50\2300_50_luminosity_electron_350000turns.csv'
    # )
    path_1Ne_xNp.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-0.9Np-不稳定-sp=10w仍未达到稳定-1023_30\1023_30_luminosity_electron_700000turns.csv'
    )

    #####
    path_1Ne_xNp_instability.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-0.9Np-不稳定-sp=10w仍未达到稳定-1023_30\1023_30_luminosity_electron_700000turns.csv'
    )
    #####

    # path_1Ne_xNp.append(
    #     r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-0.92Np-在最后似乎开始增长-1006_48\1006_48_luminosity_electron_350000turns.csv'
    # )
    path_1Ne_xNp.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-0.95Np-稳定-1507_31\1507_31_luminosity_electron_350000turns.csv'
    )
    path_1Ne_xNp.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-1Np-稳定-1538_11\1538_11_luminosity_electron_350000turns.csv'
    )
    path_1Ne_xNp.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-1.1Np-稳定-2224_18\2224_18_luminosity_electron_350000turns.csv'
    )
    path_1Ne_xNp.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-1.2Np-稳定-2225_26\2225_26_luminosity_electron_350000turns.csv'
    )
    path_1Ne_xNp.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-1.3Np-稳定-1958_50\1958_50_luminosity_electron_350000turns.csv'
    )
    path_1Ne_xNp.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-1.4Np-稳定-2115_33\2115_33_luminosity_electron_350000turns.csv'
    )
    path_1Ne_xNp.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-1.5Np-sp在25000开始不稳定-1420_02\1420_02_luminosity_electron_350000turns.csv'
    )
    # path_1Ne_xNp.append(
    #     r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-1.5Np-sp在40000开始不稳定-1126_15\1126_15_luminosity_electron_350000turns.csv'
    # )
    path_1Ne_xNp.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-1.6Np-不稳定-2317_57\2317_57_luminosity_electron_350000turns.csv'
    )
    path_1Ne_xNp.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-1.7Np-不稳定-1058_49\1058_49_luminosity_electron_350000turns.csv'
    )
    path_1Ne_xNp.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-1.8Np-不稳定-1804_15\1804_15_luminosity_electron_350000turns.csv'
    )
    path_1Ne_xNp.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-1.9Np-不稳定-1701_28\1701_28_luminosity_electron_350000turns.csv'
    )
    path_1Ne_xNp.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-2.0Np-不稳定-1936_29\1936_29_luminosity_electron_350000turns.csv'
    )

    ############################################################  4e-7p，改变电子工作点，优化质子流强极限

    path_1Ne_xNp_change_Qex.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-0.4Np-稳定-电子Qx由0.58改为0.6064-0910_57\0910_57_luminosity_electron_350000turns.csv'
    )

    path_1Ne_xNp_change_Qex.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-0.5Np-稳定-电子Qx由0.58改为0.602-2056_00\2056_00_luminosity_electron_350000turns.csv'
    )

    path_1Ne_xNp_change_Qex.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-0.6Np-稳定-电子Qx由0.58改为0.5976-2055_31\2055_31_luminosity_electron_350000turns.csv'
    )

    path_1Ne_xNp_change_Qex.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-0.7Np-稳定-电子Qx由0.58改为0.593-1140_53\1140_53_luminosity_electron_350000turns.csv'
    )

    path_1Ne_xNp_change_Qex.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-0.8Np-稳定-电子Qx由0.58改为0.5888-1834_10\1834_10_luminosity_electron_350000turns.csv'
    )

    path_1Ne_xNp_change_Qex.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-0.9Np-稳定-电子Qx由0.58改为0.5844-0206_24\0206_24_luminosity_electron_350000turns.csv'
    )

    ############################################################  4e-7p，改变质子工作点，优化质子流强极限

    path_1Ne_xNp_change_Qpx.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-0.4Np-轻微不稳定后恢复稳定-质子Qx由0.315改为0.3612-1440_45\1440_45_luminosity_electron_350000turns.csv'
    )

    path_1Ne_xNp_change_Qpx.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-0.5Np-轻微亮度损失后恢复稳定-质子Qx由0.315改为0.3535-0902_29\0902_29_luminosity_electron_350000turns.csv'
    )

    path_1Ne_xNp_change_Qpx.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-0.6Np-不稳定后在低亮度保持稳定-质子Qx由0.315改为0.3458-1633_54\1633_54_luminosity_electron_350000turns.csv'
    )

    path_1Ne_xNp_change_Qpx.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-0.7Np-出现轻微不稳定之后稳定-质子Qx由0.315改为0.3381-1633_01\1633_01_luminosity_electron_350000turns.csv'
    )

    path_1Ne_xNp_change_Qpx.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-0.8Np-稳定-质子Qx由0.315改为0.3304-后期亮度损失速度变慢-1810_50\1810_50_luminosity_electron_350000turns.csv'
    )

    path_1Ne_xNp_change_Qpx.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-0.9Np-稳定-质子Qx由0.315改为0.3227-1630_31\1630_31_luminosity_electron_350000turns.csv'
    )

    ############################################################  4e-7p，电子流强极限

    path_xNe_1Np.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\0.1Ne-1Np-稳定-0836_37/0836_37_luminosity_proton_200000turns.csv'
    )
    path_xNe_1Np.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\0.2Ne-1Np-稳定-2131_35/2131_35_luminosity_proton_200000turns.csv'
    )
    path_xNe_1Np.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\0.4Ne-1Np-稳定-1358_22/1358_22_luminosity_proton_200000turns.csv'
    )
    path_xNe_1Np.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\0.6Ne-1Np-稳定-1510_10/1510_10_luminosity_proton_200000turns.csv'
    )
    path_xNe_1Np.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\0.8Ne-1Np-稳定-0712_07/0712_07_luminosity_proton_200000turns.csv'
    )
    path_xNe_1Np.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1Ne-1Np-稳定-1538_11/1538_11_luminosity_proton_200000turns.csv'
    )
    path_xNe_1Np.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\1.5Ne-1Np-稳定-0955_12/0955_12_luminosity_proton_200000turns.csv'
    )
    path_xNe_1Np.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\2Ne-1Np-稳定-1539_35/1539_35_luminosity_proton_200000turns.csv'
    )
    path_xNe_1Np.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\2.5Ne-1Np-稳定-1014_03/1014_03_luminosity_proton_200000turns.csv'
    )
    path_xNe_1Np.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\3Ne-1Np-稳定-0826_00/0826_00_luminosity_proton_200000turns.csv'
    )
    path_xNe_1Np.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\3.5Ne-1Np-稳定-0958_20/0958_20_luminosity_proton_200000turns.csv'
    )
    path_xNe_1Np.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\4Ne-1Np-稳定-0826_10/0826_10_luminosity_proton_200000turns.csv'
    )

    ############################################################  1e-1p，质子流强极限

    path_1Ne_1Np_change_Np.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\单束团对撞-质束束极限-2022-01\1Ne-0.1Np-稳定-2nd-1628_06\1628_06_luminosity_suPeriod_500000turns.csv'
    )
    # path_1Ne_1Np_change_Np.append(
    #     r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\单束团对撞-质束束极限-2022-01\1Ne-0.1Np-稳定-0840_58\0840_58_luminosity_suPeriod_500000turns.csv'
    # )
    path_1Ne_1Np_change_Np.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\单束团对撞-质束束极限-2022-01\1Ne-0.2Np-稳定-2nd-1628_25\1628_25_luminosity_suPeriod_500000turns.csv'
    )
    # path_1Ne_1Np_change_Np.append(
    #     r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\单束团对撞-质束束极限-2022-01\1Ne-0.2Np-稳定-1047_11\1047_11_luminosity_suPeriod_500000turns.csv'
    # )
    # path_1Ne_1Np_change_Np.append(
    #     r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\单束团对撞-质束束极限-2022-01\1Ne-0.3Np-稳定-2nd-1628_35\1628_35_luminosity_suPeriod_500000turns.csv'
    # )
    path_1Ne_1Np_change_Np.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\单束团对撞-质束束极限-2022-01\1Ne-0.3Np-稳定-1048_24\1048_24_luminosity_suPeriod_500000turns.csv'
    )
    path_1Ne_1Np_change_Np.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\单束团对撞-质束束极限-2022-01\1Ne-0.4Np-稳定-2nd-1628_41\1628_41_luminosity_suPeriod_500000turns.csv'
    )
    # path_1Ne_1Np_change_Np.append(
    #     r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\单束团对撞-质束束极限-2022-01\1Ne-0.4Np-稳定-1048_38\1048_38_luminosity_suPeriod_500000turns.csv'
    # )
    path_1Ne_1Np_change_Np.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\单束团对撞-质束束极限-2022-01\1Ne-0.5Np-稳定-1048_50\1048_50_luminosity_suPeriod_500000turns.csv'
    )
    path_1Ne_1Np_change_Np.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\单束团对撞-质束束极限-2022-01\1Ne-0.6Np-稳定-1049_00\1049_00_luminosity_suPeriod_500000turns.csv'
    )
    path_1Ne_1Np_change_Np.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\单束团对撞-质束束极限-2022-01\1Ne-0.7Np-稳定-1049_15\1049_15_luminosity_suPeriod_500000turns.csv'
    )
    path_1Ne_1Np_change_Np.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\单束团对撞-质束束极限-2022-01\1Ne-0.8Np-稳定-1049_28\1049_28_luminosity_suPeriod_500000turns.csv'
    )
    path_1Ne_1Np_change_Np.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\单束团对撞-质束束极限-2022-01\1Ne-0.9Np-稳定-1049_38\1049_38_luminosity_suPeriod_500000turns.csv'
    )
    path_1Ne_1Np_change_Np.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\单束团对撞-质束束极限-2022-01\1Ne-1.0Np-稳定-1323_48\1323_48_luminosity_suPeriod_500000turns.csv'
    )
    path_1Ne_1Np_change_Np.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\单束团对撞-质束束极限-2022-01\1Ne-1.1Np-稳定-1324_12\1324_12_luminosity_suPeriod_500000turns.csv'
    )
    path_1Ne_1Np_change_Np.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\单束团对撞-质束束极限-2022-01\1Ne-1.2Np-稳定-1324_21\1324_21_luminosity_suPeriod_500000turns.csv'
    )
    path_1Ne_1Np_change_Np.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\单束团对撞-质束束极限-2022-01\1Ne-1.3Np-稳定-1324_30\1324_30_luminosity_suPeriod_500000turns.csv'
    )
    path_1Ne_1Np_change_Np.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\单束团对撞-质束束极限-2022-01\1Ne-1.4Np-稳定-1735_20\1735_20_luminosity_suPeriod_500000turns.csv'
    )
    path_1Ne_1Np_change_Np.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\单束团对撞-质束束极限-2022-01\1Ne-1.5Np-不稳定-1735_34\1735_34_luminosity_suPeriod_500000turns.csv'
    )
    path_1Ne_1Np_change_Np.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\单束团对撞-质束束极限-2022-01\1Ne-1.6Np-不稳定-1735_52\1735_52_luminosity_suPeriod_500000turns.csv'
    )
    path_1Ne_1Np_change_Np.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\单束团对撞-质束束极限-2022-01\1Ne-1.7Np-不稳定-1736_09\1736_09_luminosity_suPeriod_500000turns.csv'
    )
    path_1Ne_1Np_change_Np.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\单束团对撞-质束束极限-2022-01\1Ne-1.8Np-不稳定-1736_33\1736_33_luminosity_suPeriod_500000turns.csv'
    )
    path_1Ne_1Np_change_Np.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\单束团对撞-质束束极限-2022-01\1Ne-1.9Np-不稳定-1737_13\1737_13_luminosity_suPeriod_500000turns.csv'
    )
    path_1Ne_1Np_change_Np.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\单束团对撞-质束束极限-2022-01\1Ne-2.0Np-不稳定-1737_29\1737_29_luminosity_suPeriod_500000turns.csv'
    )

    ###### 1e-1p 不稳定
    path_1Ne_1Np_instability.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\单束团对撞-质束束极限-2022-01\1Ne-1.5Np-不稳定-1735_34\1735_34_luminosity_suPeriod_500000turns.csv'
    )
    path_1Ne_1Np_instability.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\单束团对撞-质束束极限-2022-01\1Ne-1.6Np-不稳定-1735_52\1735_52_luminosity_suPeriod_500000turns.csv'
    )
    path_1Ne_1Np_instability.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\单束团对撞-质束束极限-2022-01\1Ne-1.7Np-不稳定-1736_09\1736_09_luminosity_suPeriod_500000turns.csv'
    )
    path_1Ne_1Np_instability.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\单束团对撞-质束束极限-2022-01\1Ne-1.8Np-不稳定-1736_33\1736_33_luminosity_suPeriod_500000turns.csv'
    )
    path_1Ne_1Np_instability.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\单束团对撞-质束束极限-2022-01\1Ne-1.9Np-不稳定-1737_13\1737_13_luminosity_suPeriod_500000turns.csv'
    )
    path_1Ne_1Np_instability.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\单束团对撞-质束束极限-2022-01\1Ne-2.0Np-不稳定-1737_29\1737_29_luminosity_suPeriod_500000turns.csv'
    )

    ##################

    ############################################################  1e-1p，电子流强极限

    path_1Ne_1Np_change_Ne.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\单束团对撞-电子束束极限-2022-01\0.1Ne-1.0Np-稳定-0844_33\0844_33_luminosity_suPeriod_500000turns.csv'
    )
    path_1Ne_1Np_change_Ne.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\单束团对撞-电子束束极限-2022-01\0.2Ne-1.0Np-稳定-1738_33\1738_33_luminosity_suPeriod_500000turns.csv'
    )
    path_1Ne_1Np_change_Ne.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\单束团对撞-电子束束极限-2022-01\0.4Ne-1.0Np-稳定-1756_50\1756_50_luminosity_suPeriod_500000turns.csv'
    )
    path_1Ne_1Np_change_Ne.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\单束团对撞-电子束束极限-2022-01\0.6Ne-1.0Np-稳定-1757_06\1757_06_luminosity_suPeriod_500000turns.csv'
    )
    path_1Ne_1Np_change_Ne.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\单束团对撞-电子束束极限-2022-01\0.8Ne-1.0Np-稳定-1757_28\1757_28_luminosity_suPeriod_500000turns.csv'
    )
    path_1Ne_1Np_change_Ne.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\单束团对撞-电子束束极限-2022-01\1.0Ne-1.0Np-稳定-1323_48\1323_48_luminosity_suPeriod_500000turns.csv'
    )
    path_1Ne_1Np_change_Ne.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\单束团对撞-电子束束极限-2022-01\1.5Ne-1.0Np-稳定-1757_53\1757_53_luminosity_suPeriod_500000turns.csv'
    )
    path_1Ne_1Np_change_Ne.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\单束团对撞-电子束束极限-2022-01\2.0Ne-1.0Np-稳定-2224_45\2224_45_luminosity_suPeriod_500000turns.csv'
    )
    path_1Ne_1Np_change_Ne.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\单束团对撞-电子束束极限-2022-01\2.5Ne-1.0Np-稳定-2225_02\2225_02_luminosity_suPeriod_500000turns.csv'
    )
    path_1Ne_1Np_change_Ne.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\单束团对撞-电子束束极限-2022-01\3.0Ne-1.0Np-稳定-2225_21\2225_21_luminosity_suPeriod_500000turns.csv'
    )
    path_1Ne_1Np_change_Ne.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\单束团对撞-电子束束极限-2022-01\3.5Ne-1.0Np-稳定-2225_36\2225_36_luminosity_suPeriod_500000turns.csv'
    )
    path_1Ne_1Np_change_Ne.append(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\单束团对撞-电子束束极限-2022-01\4.0Ne-1.0Np-稳定-0843_28\0843_28_luminosity_suPeriod_500000turns.csv'
    )

    ############################################################

    Nproton_1Ne_xNp = [
        0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 1, 1.1, 1.2, 1.3,
        1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0
    ]
    # Nproton_1Ne_xNp = [
    #     0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.84, 0.88, 0.9, 0.92, 0.95, 1, 1.12,
    #     1.25, 1.36, 1.5, 1.6, 1.68, 1.75
    # ]

    Nproton_1Ne_xNp_change_Qex = [0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

    Nproton_1Ne_xNp_change_Qpx = [0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

    Nproton_xNe_1Np = [0.1, 0.2, 0.4, 0.6, 0.8, 1, 1.5, 2, 2.5, 3, 3.5, 4]

    Nproton_1Ne_1Np = [
        0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4,
        1.5, 1.6, 1.7, 1.8, 1.9, 2.0
    ]

    Nelectron_1Ne_1Np = [0.1, 0.2, 0.4, 0.6, 0.8, 1, 1.5, 2, 2.5, 3, 3.5, 4]

    endRowIndex_1Ne_xNp = [
        -1, -1, -1, 350000, -1, -1, -1, 350000, 350000, -1, -1, -1, -1, -1, -1,
        -1, -1, -1, -1, -1, -1
    ]

    endRowIndex_1Ne_1Np_change_Np = [
        350000, 350000, 350000, 350000, 350000, 350000, 350000, 350000, 350000,
        350000, 350000, 350000, 350000, 350000, 350000, 350000, 350000, 350000,
        350000, 350000
    ]

    Nproton_1Ne_xNp_instability = [0.4, 0.9]
    endRowIndex_1Ne_xNp_instability = [-1, -1]
    Nproton_1Ne_1Np_instability = [1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
    endRowIndex_1Ne_1Np_instability = [-1, -1, -1, -1, -1, -1]

    # endRowIndex_1Ne_xNp = [
    #     -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
    #     -1, -1, -1
    # ]

    # endRowIndex_1Ne_1Np_change_Np = [
    #     350000, 350000, 350000, 350000, 350000, 350000, 350000, 350000, 350000,
    #     350000, 350000, 350000, 350000, 350000, -1, -1, -1, -1, -1, -1
    # ]

    for i in range(len(path_1Ne_xNp)):
        get_lumi_loss(path_1Ne_xNp[i],
                      rate_1Ne_xNp,
                      startRowIndex=100,
                      endRowIndex=endRowIndex_1Ne_xNp[i],
                      skiprows=8)

    for path in path_1Ne_xNp_change_Qex:
        get_lumi_loss(path,
                      rate_1Ne_xNp_change_Qex,
                      startRowIndex=100,
                      skiprows=8)

    for path in path_1Ne_xNp_change_Qpx:
        get_lumi_loss(path,
                      rate_1Ne_xNp_change_Qpx,
                      startRowIndex=100,
                      skiprows=8)

    for i in range(len(path_1Ne_1Np_change_Np)):
        get_lumi_loss(path_1Ne_1Np_change_Np[i],
                      rate_1Ne_1Np_change_Np,
                      startRowIndex=100,
                      endRowIndex=endRowIndex_1Ne_1Np_change_Np[i])

    for i in range(len(path_1Ne_xNp_instability)):
        get_lumi_loss(path_1Ne_xNp_instability[i],
                      rate_1Ne_xNp_instability,
                      startRowIndex=100,
                      endRowIndex=endRowIndex_1Ne_xNp_instability[i])

    for i in range(len(path_1Ne_1Np_instability)):
        get_lumi_loss(path_1Ne_1Np_instability[i],
                      rate_1Ne_1Np_instability,
                      startRowIndex=100,
                      endRowIndex=endRowIndex_1Ne_1Np_instability[i])

    for path in path_xNe_1Np:
        get_lumi_loss(path, rate_xNe_1Np, startRowIndex=100, skiprows=5)

    for path in path_1Ne_1Np_change_Ne:
        get_lumi_loss(path,
                      rate_1Ne_1Np_change_Ne,
                      startRowIndex=100,
                      endRowIndex=200000)

    # plot_lumi_loss(Nproton_1Ne_xNp, rate_1Ne_xNp)
    # fig_1Ne_xNp, ax_1Ne_xNp = plt.subplots(figsize=(10, 7.5))

    fig_1Ne_xNp, ax_1Ne_xNp = plt.subplots()
    ax_1Ne_xNp.grid(zorder=1)
    myfontsize = 12

    ax_1Ne_xNp.plot(Nproton_1Ne_xNp,
                    rate_1Ne_xNp,
                    marker='s',
                    ls='--',
                    lw=1,
                    ms=6,
                    color='tab:blue',
                    label='4e vs. 7p',
                    zorder=4)
    ax_1Ne_xNp.plot(Nproton_1Ne_1Np,
                    rate_1Ne_1Np_change_Np,
                    marker='.',
                    ls='--',
                    lw=1,
                    ms=10,
                    color='tab:orange',
                    label=r'1e vs. 1p',
                    zorder=5)
    ax_1Ne_xNp.plot(Nproton_1Ne_xNp_change_Qpx,
                    rate_1Ne_xNp_change_Qpx,
                    marker='^',
                    ls='--',
                    lw=1,
                    ms=6,
                    color='tab:green',
                    label=r'4e vs. 7p, compensating $\nu_p^x$',
                    zorder=3)
    ax_1Ne_xNp.plot(Nproton_1Ne_xNp_change_Qex,
                    rate_1Ne_xNp_change_Qex,
                    marker='*',
                    ls='--',
                    lw=1,
                    ms=8,
                    color='tab:red',
                    label=r'4e vs. 7p, compensating $\nu_e^x$',
                    zorder=6)
    ax_1Ne_xNp.scatter(Nproton_1Ne_xNp_instability,
                       rate_1Ne_xNp_instability,
                       marker='s',
                       s=40,
                       facecolors='none',
                       edgecolors='tab:blue',
                       zorder=5)
    ax_1Ne_xNp.scatter(Nproton_1Ne_1Np_instability,
                       rate_1Ne_1Np_instability,
                       marker='.',
                       s=100,
                       facecolors='none',
                       edgecolors='tab:orange',
                       zorder=5)

    # arrowprops_1Ne_xNp = dict(arrowstyle="->",
    #                           facecolor='tab:blue',
    #                           edgecolor='tab:blue')
    # ax_1Ne_xNp.annotate('',
    #                     xy=(Nproton_1Ne_xNp_instability[0],
    #                         rate_1Ne_xNp_instability[0] * 0.8),
    #                     xycoords='data',
    #                     xytext=(Nproton_1Ne_xNp[3], rate_1Ne_xNp[3] * 2),
    #                     textcoords='data',
    #                     arrowprops=arrowprops_1Ne_xNp)
    # ax_1Ne_xNp.annotate('',
    #                     xy=(Nproton_1Ne_xNp_instability[1],
    #                         rate_1Ne_xNp_instability[1] * 1.2),
    #                     xycoords='data',
    #                     xytext=(Nproton_1Ne_xNp[8], rate_1Ne_xNp[8] * 2),
    #                     textcoords='data',
    #                     arrowprops=arrowprops_1Ne_xNp)

    ax_1Ne_xNp.set_yscale('log')
    ax_1Ne_xNp.set_xlabel(
        r'Number of proton particles $(N_p/N_{p_0})$',
        fontsize=myfontsize)
    ax_1Ne_xNp.set_ylabel(r'Luminosity loss rate', fontsize=myfontsize)

    ax_1Ne_xNp.legend(fontsize=myfontsize)

    ax_1Ne_xNp.set_ylim((1e-4, 1))
    ax_1Ne_xNp.set_xlim((0, 2.1))
    x_major_locator = plt.MultipleLocator(0.2)
    ax_1Ne_xNp.xaxis.set_major_locator(x_major_locator)
    plt.xticks(fontsize=myfontsize)
    plt.yticks(fontsize=myfontsize)

    # plt.savefig(
    #     r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\lumi loss rate.png',
    #     dpi=300)
    plt.savefig(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\proton-limit',
        dpi=300)
    plt.show()

    ##########

    # fig_xNe_1Np, ax_xNe_1Np = plt.subplots(figsize=(10, 7.5))
    fig_xNe_1Np, ax_xNe_1Np = plt.subplots()
    ax_xNe_1Np.grid()
    myfontsize = 12

    ax_xNe_1Np.plot(Nproton_xNe_1Np,
                    rate_xNe_1Np,
                    marker='s',
                    ls='--',
                    lw=1,
                    ms=6,
                    color='tab:blue',
                    label='4e vs. 7p')
    ax_xNe_1Np.plot(Nelectron_1Ne_1Np,
                    rate_1Ne_1Np_change_Ne,
                    marker='.',
                    ls='--',
                    lw=1,
                    ms=10,
                    color='tab:orange',
                    label='1e vs. 1p')
    ax_xNe_1Np.set_yscale('log')
    ax_xNe_1Np.set_xlabel(
        r'Number of electron particles $(N_e/N_{e_0})$',
        fontsize=myfontsize)
    ax_xNe_1Np.set_ylabel(r'Luminosity loss rate', fontsize=myfontsize)

    ax_xNe_1Np.legend(fontsize=myfontsize)
    # ax_xNe_1Np.set_ylim((1e-3, 0))
    plt.xticks(fontsize=myfontsize)
    plt.yticks(fontsize=myfontsize)

    # plt.savefig(
    #     r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\lumi loss rate.png',
    #     dpi=300)
    plt.savefig(
        r'D:\OneDrive\模拟数据\使用相同分布计算单束团与多束团束束极限-2021-12-09\4e-7p-多束团对撞\electron-limit',
        dpi=300)
    plt.show()
