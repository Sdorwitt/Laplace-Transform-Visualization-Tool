"""
laplace_surface_plot.py

Plots the clipped magnitude |H(s)| over a grid of s = σ + jω on a 3D axis.

The plot range is derived from the pole and zero locations of the system,
mirroring the approach used in frequency_response.py.  Values near poles
are clipped at the 95th percentile so the rest of the surface remains
readable.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D   # noqa: F401 – registers 3d projection


_GRID_POINTS  = 300   # Resolution per axis (increase for higher quality)
_CLIP_PCT     = 95    # Percentile at which to cap |H(s)| spikes near poles


def plot_laplace_surface(ax: Axes3D, num: list, den: list) -> None:
    """
    Plot a clipped |H(s)| magnitude surface on *ax*.

    Parameters:
    ax  : Matplotlib 3D axis (projection='3d').
    num : Numerator coefficients   [b2, b1, b0].
    den : Denominator coefficients [a2, a1, a0].
    """
    # Determine a sensible plot range from pole/zero locations
    zeros = np.roots(num)
    poles = np.roots(den)

    natural_freqs = np.abs(np.concatenate((zeros, poles)))
    natural_freqs = natural_freqs[natural_freqs > 0]

    plot_range = float(natural_freqs.max() * 1.5) if len(natural_freqs) else 5.0
    plot_range = max(plot_range, 1.0)   # floor so trivial systems still render

    # Build the s-plane grid
    sigma = np.linspace(-plot_range, plot_range, _GRID_POINTS)
    omega = np.linspace(-plot_range, plot_range, _GRID_POINTS)
    Sigma, Omega = np.meshgrid(sigma, omega)
    S = Sigma + 1j * Omega

    H_mag = np.abs(np.polyval(num, S) / np.polyval(den, S))

    # Clip spikes near poles so the surface is readable
    ceiling = np.percentile(H_mag, _CLIP_PCT)
    H_mag = np.clip(H_mag, 0.0, ceiling)

    surf = ax.plot_surface(Sigma, Omega, H_mag, cmap="viridis", edgecolor="none")

    ax.set_xlabel("Real  σ")
    ax.set_ylabel("Imag  ω")
    ax.set_zlabel("|H(s)|")
    ax.set_title("Laplace Magnitude Surface")
