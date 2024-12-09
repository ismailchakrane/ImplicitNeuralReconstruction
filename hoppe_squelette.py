import numpy as np
import mcubes
from scipy import spatial

# Load the oriented point set
p = np.loadtxt('armadillo_sub.xyz')

# Compute the enclosing grid
min_bound = np.min(p, axis=0)
max_bound = np.max(p, axis=0)

grid_size = 128

X, Y, Z = np.mgrid[
    min_bound[0]:max_bound[0]:grid_size * 1j,
    min_bound[1]:max_bound[1]:grid_size * 1j,
    min_bound[2]:max_bound[2]:grid_size * 1j
]

# Build a KDTree encoding this point set
kdtree = spatial.KDTree(p[:, :3]) 

# Initialize the signed distance grid
u = np.zeros_like(X)

# Compute the signed distance values for each point in the grid
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        for k in range(X.shape[2]):
            point = np.array([X[i, j, k], Y[i, j, k], Z[i, j, k]])
            dist, idx = kdtree.query(point)
            nearest_point = p[idx, :3]
            nearest_normal = p[idx, 3:]
            sign = np.sign(np.dot(point - nearest_point, nearest_normal))
            u[i, j, k] = sign * dist

# Extract the 0-level set using marching cubes
vertices, triangles = mcubes.marching_cubes(u, 0)

# Save and visualize the mesh
mcubes.export_obj(vertices, triangles, 'result_hoppe.obj')