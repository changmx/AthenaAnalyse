import numpy as np
import matplotlib.pyplot as plt


def plot_hourglass_factor(ax,
                          sigma,
                          theory,
                          sim,
                          title,
                          sim_label='Simulated result',
                          theory_label='Theoretical value'):
    sigma = sigma * 100
    ax.scatter(sigma, sim, label=sim_label)
    ax.plot(sigma, theory, label=theory_label, color='orange')

    error = [0] * sigma.shape[0]
    sum_error = 0

    for i in range(sigma.shape[0]):
        error[i] = abs(sim[i] - theory[i]) / theory[i]
        sum_error += error[i]

    ax.text(2,
            sim[0],
            r'$Average\ relative\ error = $' +
            str(format(sum_error / (sigma.shape[0]) * 100, ".2f")) + '%',
            bbox=dict(boxstyle="round", fc="w"),
            fontsize='medium')

    ax.locator_params("x", tight=True, nbins=10)
    ax.set_xlabel(r'$\sigma_z\ (cm)$', loc='center')
    ax.set_ylabel('hourglass factor')
    ax.set_ylim(0.6, 1.05)
    ax.set_title(title)
    ax.grid()
    ax.legend()


if __name__ == '__main__':
    sigma_z1_change, theory_z1_change, sim_10slices_z1_change, sigma_z2_change, theory_z2_change, sim_10slices_z2_change, sim_20slices_z2_change, sigma_z1z2_change, theory_z1z2_change, sim_10slices_z1z2_change, sim_20slices_z1z2_change = np.loadtxt(
        r'D:\研究生\博二\2021_04_hourglass因子对比\hourglass_compare2.csv',
        delimiter=',',
        skiprows=1,
        usecols=(0, 1, 2, 4, 5, 6, 7, 9, 10, 11, 12),
        unpack=True)

    fig, ax = plt.subplots(1, 3, sharex=True)
    plot_hourglass_factor(
        ax[0],
        sigma_z1_change,
        theory_z1_change,
        sim_10slices_z1_change,
        title=
        r'Change $\sigma_p$ and keep $\sigma_e = {0}cm$, 10 slices per beam'.
        format(2))

    plot_hourglass_factor(
        ax[1],
        sigma_z2_change,
        theory_z2_change,
        sim_10slices_z2_change,
        title=
        r'Change $\sigma_e$ and keep $\sigma_p = {0}cm$, 10 slices per beam'.
        format(4))

    plot_hourglass_factor(
        ax[2],
        sigma_z1z2_change,
        theory_z1z2_change,
        sim_10slices_z1z2_change,
        title=r'Change $\sigma_e$ and $\sigma_p$, 10 slices per beam')

    plt.show()
