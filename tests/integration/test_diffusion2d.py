"""
Tests for functionality checks in class SolveDiffusion2D
"""
import numpy as np
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from diffusion2d import SolveDiffusion2D


def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_physical_parameters
    """
    solver = SolveDiffusion2D()
    w, h, dx, dy = 30., 40., 0.2, 0.2
    d, T_cold, T_hot = 4., 100., 300.
    expected_dt = 0.0025

    solver.initialize_domain(w, h, dx, dy)
    solver.initialize_physical_parameters(d, T_cold, T_hot)

    assert np.allclose(expected_dt, solver.dt), f"Expected dt={expected_dt}, but is {solver.dt}"


def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.set_initial_condition
    """
    solver = SolveDiffusion2D()

    solver.initialize_domain(30., 40., 0.2, 0.2)
    solver.initialize_physical_parameters(4., 100., 300.)
    solver_u = solver.set_initial_condition()

    dx,dy,T_cold,T_hot = 0.2, 0.2, 100., 300.
    r, cx, cy, nx, ny = 2, 5, 5, 150, 200
    r2 = r ** 2

    u = T_cold * np.ones((nx, ny))

    for i in range(nx):
        for j in range(ny):
            p2 = (i * dx - cx) ** 2 + (j * dy - cy) ** 2
            if p2 < r2:
                u[i, j] = T_hot

    assert np.allclose(solver_u, u), f"u should be {u},but got{solver_u}"
                
