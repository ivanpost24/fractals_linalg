import matplotlib.pyplot as plt  # Plotting functions
import numpy as np  # Array and matrix representation


# --- Constants ---
# I use ALL CAPS to differentiate between normal variables. We declare them in the global scope (i.e., outside any
# function) so we can use them anywhere. We shouldn't ever mutate these values because we trust that they won't change.
ITERATIONS = 100000  # Number of points to generate
SIDES = 3  # Number of sides of the regular polygon


# I put all the code in a main function instead of the global scope because it makes it easier to add more code later.
# In general, you shouldn't be putting anything but functions (like this one), type declarations, and constants in the
# global scope.
def main() -> None:
    rng = np.random.default_rng()  # Create a random number generator

    # --- Get the vertices of the regular polygon ---
    t = np.linspace(0, 2 * np.pi, SIDES + 1)[:-1]  # Gets evenly separated values from 0 to 2*pi
    #                                        ^ Omit the last one (since 0 == 2*pi)
    # Create a numpy array that contains our points. The first index is the vertex index, and the second is the
    # vector component index.
    v = np.array([np.cos(t), np.sin(t)]).T
    #                                    ^ Transpose because the indices are reversed

    # --- Create a transformation matrix ---
    T = np.array([[0.5, 0.0],
                  [0.0, 0.5]])

    # --- Prepare point array ---
    x = np.zeros(shape=(ITERATIONS + 1, 2))  # Start with an array of zeros
    x[0] = rng.uniform(-0.5, 0.5, size=2)  # Randomly select the first point (remember Python is 0-indexed)

    # --- Generate the points to form the Sierpinski triangle ---
    for i in range(ITERATIONS):
        k = rng.integers(SIDES)  # Choose a vertex (index) at random
        # The next point is somewhere in between the vertex and the current point (currently half-way)
        x[i + 1] = T @ (x[i] - v[k]) + v[k]
        #            ^ Matrix multiplication (the standard multiplication operator * doesn't work)

    # --- Plotting ---
    fig, ax = plt.subplots()  # Create a figure and axes
    ax.plot(x[:, 0], x[:, 1], '.', markersize=0.1)  # Plot the points
    #         ^               ^    ^ This keyword argument reduces the marker size to increase the resolution of the
    #         |               |      triangle
    #         |               | This makes it so that there are no lines connecting each point
    #         | This is called a "slice," and in this case it takes all the values in the first index
    #           (i.e. all the points). We're separating the second index into 0 and 1 because those are the x and y
    #           coordinates, respectively.

    ax.set_aspect('equal')  # Make the scale of the axes equal

    plt.show()  # Display the plot in a new window (you have to close the window to end the program)


if __name__ == '__main__':  # Don't worry about what this does
    main()
