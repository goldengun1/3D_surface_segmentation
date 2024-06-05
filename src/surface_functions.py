import numpy as np

FUNCTION_COUNT = 8
FUNCTION_NAMES = [
    "Surface1 Function",
    "Surface2 Function",
    "Ackley Function",
    "Rastrigin Function",
    "Rosenbrock Function",
    "Himmelblau Function",
    "Goldstein Price Function",
    "Michalewicz Function",
]


def ackley_function(x, y):
    """
    The Ackley function is a multimodal function often used for testing optimization algorithms.
    It is defined as: f(x, y) = -20 * exp(-0.2 * sqrt(0.5 * (x^2 + y^2))) - exp(0.5 * (cos(2πx) + cos(2πy))) + e + 20

    Parameters:
    x (float): The x-coordinate of the point to evaluate the function.
    y (float): The y-coordinate of the point to evaluate the function.

    Returns:
    float: The value of the Ackley function at the given point (x, y).

    Note:
    The function has a global minimum at: (x, y) = (0, 0)
    The function is periodic with periodicity 2π in both x and y directions.
    """
    part1 = -20 * np.exp(-0.2 * np.sqrt(0.5 * (x**2 + y**2)))
    part2 = -np.exp(0.5 * (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y)))
    return part1 + part2 + np.e + 20


def rastrigin_function(x, y):
    """
    The Rastrigin function is a non-convex, multimodal function often used for testing optimization algorithms.
    It is defined as: f(x, y) = 20 + x^2 + y^2 - 10 * (cos(2πx) + cos(2πy))

    Parameters:
    x (float): The x-coordinate of the point to evaluate the function.
    y (float): The y-coordinate of the point to evaluate the function.

    Returns:
    float: The value of the Rastrigin function at the given point (x, y).

    Note:
    The function has a global minimum at: (x, y) = (0, 0)
    The function is periodic with periodicity 1 in both x and y directions.
    """
    return 20 + x**2 + y**2 - 10 * (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y))


def rosenbrock_function(x, y):
    """
    The Rosenbrock function is a non-convex function used for testing optimization algorithms.
    It is defined as: f(x, y) = (1 - x)^2 + 100(y - x^2)^2

    Parameters:
    x (float): The x-coordinate of the point to evaluate the function.
    y (float): The y-coordinate of the point to evaluate the function.

    Returns:
    float: The value of the Rosenbrock function at the given point (x, y).

    Note:
    The function has a global minimum at: (x, y) = (1, 1)
    """
    return (1 - x) ** 2 + 100 * (y - x**2) ** 2


def himmelblau_function(x, y):
    """
    The Himmelblau's function is a multimodal function used for testing optimization algorithms.
    It is defined as: f(x, y) = (x^2 + y - 11)^2 + (x + y^2 - 7)^2

    Parameters:
    x (float): The x-coordinate of the point to evaluate the function.
    y (float): The y-coordinate of the point to evaluate the function.

    Returns:
    float: The value of the Himmelblau's function at the given point (x, y).

    Note:
    The function has four global minima at:
    (x, y) = (3.0, 2.0), (-2.805118, 3.131312), (-3.779310, -3.283186), (3.584428, -1.848123)
    """
    return (x**2 + y - 11) ** 2 + (x + y**2 - 7) ** 2


def goldstein_price_function(x, y):
    """
    The Goldstein-Price function is a non-convex function used for testing optimization algorithms.
    It is defined as: f(x, y) = (1 + (x + y + 1)^2 * (19 - 14x + 3x^2 - 14y + 6xy + 3y^2)) * (30 + (2x - 3y)^2 * (18 - 32x + 12x^2 + 48y - 36xy + 27y^2))

    Parameters:
    x (float): The x-coordinate of the point to evaluate the function.
    y (float): The y-coordinate of the point to evaluate the function.

    Returns:
    float: The value of the Goldstein-Price function at the given point (x, y).

    Note:
    The function has a global minimum at: (x, y) = (0, -1)
    The function is periodic with periodicity 2π in both x and y directions.
    """
    term1 = 1 + (x + y + 1) ** 2 * (
        19 - 14 * x + 3 * x**2 - 14 * y + 6 * x * y + 3 * y**2
    )
    term2 = 30 + (2 * x - 3 * y) ** 2 * (
        18 - 32 * x + 12 * x**2 + 48 * y - 36 * x * y + 27 * y**2
    )
    return term1 * term2


def michalewicz_function(x, y, m=10):
    """
    The Michalewicz function is a multimodal function often used for testing optimization algorithms.
    It is defined as: f(x, y) = -sin(x) * (sin(x^2 / π))^(2m) - sin(y) * (sin(2y^2 / π))^(2m)

    Parameters:
    x (float): The x-coordinate of the point to evaluate the function.
    y (float): The y-coordinate of the point to evaluate the function.
    m (int, optional): The parameter that controls the steepness of the function's valleys. Default is 10.

    Returns:
    float: The value of the Michalewicz function at the given point (x, y).

    Note:
    The function has a global minimum at: (x, y) = (2.2029, 1.5708)
    The function is periodic with periodicity π in both x and y directions.
    """
    term1 = -np.sin(x) * (np.sin(x**2 / np.pi)) ** (2 * m)
    term2 = -np.sin(y) * (np.sin(2 * y**2 / np.pi)) ** (2 * m)
    return term1 + term2


def surface1(X, Y):
    return (1.2 + np.cos(0.1 * (X**2 + Y**2)) + 0.01 * (X**2 + Y**2)) - 1


def surface2(x, y):
    return np.sin(x**2 + y**2)
