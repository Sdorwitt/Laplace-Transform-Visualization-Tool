"""
Laplace Transform Visualisation Tool

Accepts coefficients for a second-order LTI system of the form:
 
    a2·y'' + a1·y' + a0·y  =  b2·x'' + b1·x' + b0·x
 
and produces five plots:
  1. 3D Laplace magnitude surface  |H(s)|
  2. Pole-zero diagram
  3. Bode magnitude      |H(jω)|
  4. Bode phase          ∠H(jω)
  5. Impulse response    h(t)
"""
 
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
 
from poles_and_zeros import plot_pz
from frequency_response import plot_freq_response
from laplace_surface_plot import plot_laplace_surface
from time_domain_impulse_plot import plot_time_response
 
 
def parse_coefficients() -> list[float]:
    # Prompt the user for six coefficients and return them as floats.
    prompt = (
        "Enter coefficients a2 a1 a0 b2 b1 b0 (space-separated)\n"
        "for:  a2·y'' + a1·y' + a0·y = b2·x'' + b1·x' + b0·x\n> "
    )
    try:
        raw = input(prompt)
        coeffs = [float(v) for v in raw.split()]
    except ValueError:
        sys.exit("Error: all coefficients must be numeric.")
 
    if len(coeffs) != 6:
        sys.exit(f"Error: expected 6 coefficients, got {len(coeffs)}.")
 
    return coeffs
 
 
def main() -> None:
    coeffs = parse_coefficients()
    a2, a1, a0, b2, b1, b0 = coeffs
 
    num = [b2, b1, b0]
    den = [a2, a1, a0]
 
    # Poles and zeros of H(s) = Num(s) / Den(s)
    poles = np.roots(den)
    zeros = np.roots(num)
 
    # Layout:
    fig = plt.figure(figsize=(14, 11))
    gs = gridspec.GridSpec(
        4, 2,
        width_ratios=[2.5, 1],
        wspace=0.45,
        hspace=1,    
    )
 
    ax_laplace = fig.add_subplot(gs[:, 0], projection="3d")
    ax_pz      = fig.add_subplot(gs[0, 1])
    ax_mag     = fig.add_subplot(gs[1, 1])
    ax_phase   = fig.add_subplot(gs[2, 1], sharex=ax_mag)
    ax_time    = fig.add_subplot(gs[3, 1])

    # Plots
    plot_laplace_surface(ax_laplace, num, den)
    plot_pz(ax_pz, poles, zeros)
    plot_freq_response(ax_mag, ax_phase, b2, b1, b0, a2, a1, a0)
    plot_time_response(ax_time, num, den, t_end=10)
 
    fig.suptitle("Laplace Transform Visualisation", fontsize=14, fontweight="bold")
    plt.show()
 
 
if __name__ == "__main__":
    main()