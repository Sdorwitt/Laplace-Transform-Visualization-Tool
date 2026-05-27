"""
frequency_response.py

Computes and plots the full Bode response of a second-order transfer function
 
    H(s) = (b2·s² + b1·s + b0) / (a2·s² + a1·s + a0)
 
evaluated along the imaginary axis  s = jω.
 
Two axes are required: one for magnitude |H(jω)|, one for phase ∠H(jω).
"""
 
import numpy as np
import matplotlib.pyplot as plt
 
 
def _H(b2: float, b1: float, b0: float,
       a2: float, a1: float, a0: float,
       w: np.ndarray) -> np.ndarray:
    """Return H(jω) for each frequency in *w*."""
    s = 1j * w
    return (b2*s**2 + b1*s + b0) / (a2*s**2 + a1*s + a0)
 
 
def _freq_range(b2: float, b1: float, b0: float,
                a2: float, a1: float, a0: float) -> tuple[float, float]:
    """Return (w_min, w_max) derived from pole/zero natural frequencies."""
    natural_freqs = np.abs(np.concatenate((
        np.roots([b2, b1, b0]),
        np.roots([a2, a1, a0]),
    )))
    natural_freqs = natural_freqs[natural_freqs > 0]
 
    if len(natural_freqs) == 0:
        return 0.1, 100.0
    return natural_freqs.min() / 10.0, natural_freqs.max() * 10.0
 
 
def plot_freq_response(ax_mag: plt.Axes, ax_phase: plt.Axes,
                       b2: float, b1: float, b0: float,
                       a2: float, a1: float, a0: float) -> None:
    """
    Plot the Bode magnitude and phase of H(jω) on two separate axes.
 
    Parameters:
    ax_mag, ax_phase : Axes for magnitude and phase respectively.
    b2, b1, b0       : Numerator coefficients (highest power first).
    a2, a1, a0       : Denominator coefficients (highest power first).
    """
    w_min, w_max = _freq_range(b2, b1, b0, a2, a1, a0)
    w = np.logspace(np.log10(w_min), np.log10(w_max), 5000)
    H = _H(b2, b1, b0, a2, a1, a0, w)
 
    magnitude = np.abs(H)
    phase_deg = np.angle(H, deg=True)
 
    # Magnitude
    ax_mag.plot(w, magnitude, color="steelblue", linewidth=1.5)
    ax_mag.set_xscale("log")
    ax_mag.set_ylabel("|H(jω)|")
    ax_mag.set_title("Frequency Response")
    ax_mag.grid(True, which="both", linestyle=":", linewidth=0.5)
    ax_mag.tick_params(labelbottom=False)   # shared x-axis; hide ticks on top plot
 
    # Phase
    ax_phase.plot(w, phase_deg, color="darkorange", linewidth=1.5)
    ax_phase.set_xscale("log")
    ax_phase.set_xlabel("Frequency ω (rad/s)")
    ax_phase.set_ylabel("∠H(jω)  (°)")
    ax_phase.set_yticks([-180, -90, 0, 90, 180])
    ax_phase.grid(True, which="both", linestyle=":", linewidth=0.5)