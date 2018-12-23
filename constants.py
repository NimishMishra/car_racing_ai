import numpy as np

# This array defines the vertices of the shape we want our image to have.
# Every pixel outside this shape will be darkened.
path_vertices = np.array([[0, 600],
            [0, 272],
            [240, 172],
            [560, 172],
            [800, 272],
            [800, 600]
            ])
