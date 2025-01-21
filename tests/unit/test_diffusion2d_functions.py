"""
Tests for functions in class SolveDiffusion2D
"""
import numpy as np
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from diffusion2d import SolveDiffusion2D
import unittest

class TestDiffusion2D(unittest.TestCase):
    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(w=30.,h=40.,dx=0.2,dy=0.1)
        
        self.assertEqual(solver.nx, 150, f"Expected nx=150, but got {solver.nx}")
        self.assertEqual(solver.ny, 400, f"Expected ny=400, but got {solver.ny}")

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.w = 30.
        solver.h = 40.
        solver.dx = 0.2
        solver.dy = 0.2
        solver.initialize_physical_parameters(d=4., T_cold=100., T_hot=300.)

        expected_dt = 0.0025
        self.assertAlmostEqual(solver.dt, expected_dt, places=4,msg = f"Expected dt={expected_dt}, but is {solver.dt}")

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()

        solver.dx = solver.dy = 0.2
        solver.nx = solver.ny = 50
        solver.T_cold, solver.T_hot = 200., 600.

        solver_u = solver.set_initial_condition()

        r, cx, cy = 2, 5, 5
        r2 = r ** 2

        u = solver.T_cold * np.ones((solver.nx, solver.ny))

        for i in range(solver.nx):
            for j in range(solver.ny):
                p2 = (i * solver.dx - cx) ** 2 + (j * solver.dy - cy) ** 2
                if p2 < r2:
                    u[i, j] = solver.T_hot


        for i in range(solver.nx):
            for j in range(solver.ny):
                self.assertAlmostEqual(solver_u[i, j], u[i, j], places=4,
                                       msg=f"u[{i},{j}] should be {u[i, j]},but got{solver_u[i, j]}")