# ImplicitNeuralReconstruction

This repository is part of my Master’s Degree in Artificial Intelligence at Claude Bernard University
Lyon 1. It is based on practical work, focusing on reconstructing 3D shapes from point sets. Detailed instructions are available <a href="https://perso.liris.cnrs.fr/julie.digne/cours/tp_inr.pdf" target="_blank">here</a>.

## Traditional Reconstruction Approach

The first part of this work implements the Hoppe method [Hoppe 1992], a baseline for surface reconstruction. Key steps include:

1. Loading an oriented point cloud.
2. Building a k-d tree using `scipy.spatial.KDTree`.
3. Creating a 3D grid using `numpy`.
4. Computing the signed distance function (SDF) for each grid point.
5. Extracting the 0-level set (isosurface) using `mcubes.marching_cubes`.
6. Saving and visualizing the mesh using `mcubes.export_obj`.

These steps are implemented in `hoppe_squelette.py`.
The output mesh will be saved as `result_hoppe.obj` and can be visualized with 3D software like Blender.

## Setup

### Create a Virtual Environment

Use `conda` for example to manage a Python environment:

```bash
conda create -n tp_inr
conda activate tp_inr
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Running the Code

Run for example the Hoppe reconstruction script:

```bash
python hoppe_squelette.py
```
