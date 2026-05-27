"""
poles_and_zeros.py
------------------
Plots poles (×) and zeros (○) of a transfer function on the complex plane,
with dashed lines from the origin showing each point's distance.
"""

import numpy as np
import matplotlib.pyplot as plt


def plot_pz(ax: plt.Axes, poles: np.ndarray, zeros: np.ndarray) -> None:
    """
    Draw a pole-zero diagram on *ax*.

    Parameters
    ----------
    ax     : Axes on which to draw.
    poles  : Complex array of pole locations.
    zeros  : Complex array of zero locations.
    """
    poles = np.asarray(poles, dtype=complex)
    zeros = np.asarray(zeros, dtype=complex)

    # --- Distance lines ---------------------------------------------------
    for p in poles:
        ax.plot([0, p.real], [0, p.imag], linestyle="--", color="steelblue", linewidth=0.9)
    for z in zeros:
        ax.plot([0, z.real], [0, z.imag], linestyle=":",  color="darkorange", linewidth=0.9)

    # --- Markers ----------------------------------------------------------
    if len(poles):
        ax.scatter(poles.real, poles.imag,
                   marker="x", s=120, linewidths=2,
                   color="steelblue", label="Poles", zorder=3)
    if len(zeros):
        ax.scatter(zeros.real, zeros.imag,
                   marker="o", s=130,
                   facecolors="none", edgecolors="darkorange", linewidths=2,
                   label="Zeros", zorder=3)

    # --- Axes & formatting ------------------------------------------------
    ax.axhline(0, color="black", linewidth=0.7)
    ax.axvline(0, color="black", linewidth=0.7)
    ax.set_xlabel("Real")
    ax.set_ylabel("Imaginary")
    ax.set_title("Pole-Zero Plot")
    ax.set_aspect("equal", "box")
    ax.grid(True, linestyle=":", linewidth=0.5)

    all_pts = np.concatenate((poles, zeros)) if len(poles) + len(zeros) else np.array([1+0j])
    margin = np.max(np.abs(all_pts)) * 1.4
    ax.set_xlim(-margin, margin)
    ax.set_ylim(-margin, margin)

    ax.legend(
        fontsize=8,
        loc='upper left',
        bbox_to_anchor=(1, 1)
    )

