import gudhi as gd


def enumerate_point(i: int, j: int, dim: int) -> int:
    """
    Enumerate a point in a 2D grid to a unique integer.

    Parameters:
    i (int): The row index of the point in the grid.
    j (int): The column index of the point in the grid.
    dim (int): The dimension of the grid.

    Returns:
    int: The unique integer representing the point in the grid.

    The function uses a simple linear mapping to convert a 2D grid coordinate to a unique integer.
    If the row index is 0, the mapping is straightforward: (i * dim) + j.
    If the row index is not 0, an offset is added to the mapping to ensure uniqueness: (i * dim) + j + 1.
    """
    return (i * dim) + j if i == 0 else (i * dim) + j + 1


def create_simplex_tree(X, Z):
    simplex_tree = gd.SimplexTree()
    dim = X.shape[0]

    # Insert vertices and edges of the 2D grid with filtration values as the height
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            simplex_tree.insert([enumerate_point(i, j, dim)], filtration=Z[i, j])
            if i > 0:
                simplex_tree.insert(
                    [enumerate_point(i - 1, j, dim), enumerate_point(i, j, dim)],
                    filtration=max(Z[i - 1, j], Z[i, j]),
                )
            if j > 0:
                simplex_tree.insert(
                    [enumerate_point(i, j - 1, dim), enumerate_point(i, j, dim)],
                    filtration=max(Z[i, j - 1], Z[i, j]),
                )

    # Insert 2-simplices (triangles)
    for i in range(X.shape[0] - 1):
        for j in range(X.shape[1] - 1):
            simplex_tree.insert(
                [
                    enumerate_point(i, j, dim),
                    enumerate_point(i + 1, j, dim),
                    enumerate_point(i, j + 1, dim),
                ],
                filtration=max(Z[i, j], Z[i + 1, j], Z[i, j + 1]),
            )
            simplex_tree.insert(
                [
                    enumerate_point(i + 1, j, dim),
                    enumerate_point(i, j + 1, dim),
                    enumerate_point(i + 1, j + 1, dim),
                ],
                filtration=max(Z[i + 1, j], Z[i, j + 1], Z[i + 1, j + 1]),
            )

    return simplex_tree


def create_simplex_tree_detailed(X, Z):
    simplex_tree = gd.SimplexTree()
    dim = X.shape[0]

    # Insert vertices
    for i in range(dim):
        for j in range(dim):
            simplex_tree.insert([enumerate_point(i, j, dim)], filtration=Z[i, j])

    # Insert edges of the 2D grid with filtration values as the height
    # Step 1: side to side
    for i in range(dim):
        for j in range(dim - 1):
            simplex_tree.insert(
                [enumerate_point(i, j, dim), enumerate_point(i, j + 1, dim)],
                filtration=max(Z[i, j], Z[i, j + 1]),
            )
    # Step 2: top to bottom
    for j in range(dim):
        for i in range(dim - 1):
            simplex_tree.insert(
                [enumerate_point(i, j, dim), enumerate_point(i + 1, j, dim)],
                filtration=max(Z[i, j], Z[i + 1, j]),
            )
    # Step 3: diagonal
    for i in range(dim - 1):
        for j in range(dim - 1):
            simplex_tree.insert(
                [enumerate_point(i, j, dim), enumerate_point(i + 1, j + 1, dim)],
                filtration=max(Z[i, j], Z[i + 1, j + 1]),
            )

    # Insert 2-simplices (triangles) same as other function
    for i in range(X.shape[0] - 1):
        for j in range(X.shape[1] - 1):
            simplex_tree.insert(
                [
                    enumerate_point(i, j, dim),
                    enumerate_point(i + 1, j, dim),
                    enumerate_point(i, j + 1, dim),
                ],
                filtration=max(Z[i, j], Z[i + 1, j], Z[i, j + 1]),
            )
            simplex_tree.insert(
                [
                    enumerate_point(i + 1, j, dim),
                    enumerate_point(i, j + 1, dim),
                    enumerate_point(i + 1, j + 1, dim),
                ],
                filtration=max(Z[i + 1, j], Z[i, j + 1], Z[i + 1, j + 1]),
            )

    return simplex_tree
