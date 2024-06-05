import networkx as nx


# Contour tree construction
def build_contour_tree(Z):
    """
    Constructs a contour tree from a 2D scalar field represented by a 2D array Z.

    Parameters:
    Z (numpy.ndarray): A 2D array representing the scalar field.

    Returns:
    G (networkx.Graph): A graph representing the contour tree.
    contours (list): A list of root nodes in the contour tree.

    The contour tree is constructed by performing a depth-first search on the scalar field,
    connecting adjacent points with the same value into a contour. Each contour is represented
    as a connected component in the graph.
    """

    # Initialize an empty graph
    G = nx.Graph()

    # Generate a list of points in the scalar field
    points = [(i, j) for i in range(Z.shape[0]) for j in range(Z.shape[1])]

    # Sort the points based on their scalar values
    sorted_points = sorted(points, key=lambda p: Z[p])

    # Initialize a dictionary to store the parent of each point
    parent = {}

    # Initialize a set to store the root nodes of the contour tree
    contours = set()

    # Iterate over the sorted points
    for p in sorted_points:
        x, y = p
        current_parent = p

        # Check the neighbors of the current point
        if x > 0 and (x - 1, y) in parent:
            current_parent = parent[(x - 1, y)]
        if y > 0 and (x, y - 1) in parent:
            if (x - 1, y) in parent and parent[(x - 1, y)] != parent[(x, y - 1)]:
                # If the neighbors have different parents, merge them
                G.add_edge(parent[(x - 1, y)], parent[(x, y - 1)])
                if parent[(x - 1, y)] in contours:
                    contours.remove(parent[(x - 1, y)])
                parent[(x - 1, y)] = parent[(x, y - 1)]
            current_parent = parent[(x, y - 1)]

        # Assign the parent to the current point
        parent[p] = current_parent
        contours.add(current_parent)

    # Return the contour tree graph and the root nodes
    return G, list(contours)
