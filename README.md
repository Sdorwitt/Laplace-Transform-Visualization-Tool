# Laplace-Transform-Visualization-Tool
--------Laplace Transform Visualisation tool--------

Welcome to the laplace transform visualisation tool guide. The tool works
in the following way: the user inputs the parameters of a differential equation 
and the code outputs four graphs:

1. 2d graph of the poles and zeros of the system
2. 2d graph of the bode magnitude response (x axis = frequency)
3. 2d graph of the bode angle response (x axis = frequency)
4. 2d graph of the impulse response (x axis = time)
5. 3d graph of the laplace transform (most all encompassing graph)

In order to use the tool, go to the file main.py and run the code in your python environment. 
The code will ask for your inputs and afterwards produce the graphs.

Here are some interesting inputs that will give you an idea of how the tool
can help you visualize and learn to see differential equations in terms of 
the laplace transform:

a2   a1   a0   b2   b1   b0    filter type
1    100  2500 1    0    0     high pass around 50 
1    100  2500 0    0    2500  low pass around 50     
1    .5   2500 0    .5   0     band pass around 50
1    .5   2500 1    0    2500  band stop around 50
5    10   2500 0    10   0     lower quality band pass also around 50
5    10   2500 5    0    2500  lower quality band stop also around 50

Notice the following things: 

    Band-pass vs band-stop:
        These are formed by matching the y-side and x-side coefficients and then
        zeroing either just the y' term (band-pass) or both the y and y'' terms
        (band-stop). The symmetry between the two is made very visible by the
        pole-zero diagram.
    
    Filter quality (Q factor):
        The Q factor is controlled by a1 (the damping coefficient). A smaller a1
        produces a sharper, higher-Q filter. Compare the 0.5 and 10 rows above
        and watch how the peak in the frequency response and the spike in the
        Laplace surface both narrow as a1 decreases.
    
    Pole distance from the imaginary axis:
        The closer the poles sit to the imaginary axis (small real part), the
        sharper and more resonant the filter. You can read this directly off the
        pole-zero plot and see its consequence in both the frequency response and
        the height of the Laplace surface spike.
    
    The 3D Laplace surface:
        The surface shows |H(s)| across the entire complex plane, not just along
        the imaginary axis. The frequency response graph is literally a vertical
        slice of this surface taken at σ = 0. Poles appear as peaks and zeros
        appear as valleys. Viewing both together builds an intuition for why the
        frequency response looks the way it does.

These are some observations that can be made using the tool and can help to 
achieve a geometric understanding of the equations

