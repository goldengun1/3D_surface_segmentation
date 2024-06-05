from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from typing import List, Tuple


def plot_3d_surface(
    X: List[int], Y: List[int], Z: List[int], contours: List[Tuple[int, int]]
):
    """
    This function plots a 3D surface with given X, Y, Z coordinates and highlights specified contours.

    Parameters:
    X (List[int]): A list of X coordinates for the 3D surface.
    Y (List[int]): A list of Y coordinates for the 3D surface.
    Z (List[int]): A list of Z coordinates for the 3D surface.
    contours (List[Tuple[int, int]]): A list of tuples, where each tuple contains the indices (x, y) of the contour points to be highlighted.

    Returns:
    None. The function displays the plot using matplotlib.pyplot.show().
    """
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(X, Y, Z, cmap="viridis", alpha=0.5)

    for contour in contours:
        x, y = contour
        ax.scatter(X[x, y], Y[x, y], Z[x, y], color="r")

    plt.show()
