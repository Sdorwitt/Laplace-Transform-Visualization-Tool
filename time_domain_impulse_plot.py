"""
time_domain_impulse_plot.py

Plots the impulse response h(t) of a transfer function H(s) = Num(s)/Den(s).
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


def plot_time_response(ax: plt.Axes, num: list, den: list,
                       t_end: float = 10.0, num_points: int = 1000) -> None:
    """
    Plot the impulse response of H(s) on *ax*.

    Parameters:
    ax         : Axes on which to draw.
    num        : Numerator coefficients   [b2, b1, b0].
    den        : Denominator coefficients [a2, a1, a0].
    t_end      : Length of simulation in seconds.
    num_points : Number of time samples.
    """
    system = signal.TransferFunction(num, den)
    t = np.linspace(0, t_end, num_points)

    t_out, y = signal.impulse(system, T=t)

    ax.plot(t_out, y, color="steelblue", linewidth=1.5)
    ax.axhline(0, color="black", linewidth=0.7)
    ax.set_xlabel("Time  t (s)")
    ax.set_ylabel("Amplitude")
    ax.set_title("Impulse Response")
    ax.grid(True, linestyle=":", linewidth=0.5)
