# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/05_testing_and_ci/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

#### unit

================================================= test session starts =================================================
platform win32 -- Python 3.12.8, pytest-8.3.4, pluggy-1.5.0
rootdir: C:\Users\sora\Documents\Lecture\SSE\Exercise\ex6\testing-python-exercise-wt2425
collected 3 items

tests\unit\test_diffusion2d_functions.py FFF                                                                     [100%]

====================================================== FAILURES =======================================================
_______________________________________________ test_initialize_domain ________________________________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(w=30.,h=40.,dx=0.2,dy=0.1)

>       assert solver.nx == 150, f"Expected nx=150, but is {solver.nx}"
E       AssertionError: Expected nx=150, but is 300
E       assert 300 == 150
E        +  where 300 = <diffusion2d.SolveDiffusion2D object at 0x000002355456C3B0>.nx

tests\unit\test_diffusion2d_functions.py:18: AssertionError
_________________________________________ test_initialize_physical_parameters _________________________________________

    def test_initialize_physical_parameters():
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
>       assert abs(solver.dt - expected_dt) < 1e-4, f"Expected dt={expected_dt}, but is {solver.dt}"
E       AssertionError: Expected dt=0.0025, but is 0.0075000000000000015
E       assert 0.005000000000000001 < 0.0001
E        +  where 0.005000000000000001 = abs((0.0075000000000000015 - 0.0025))
E        +    where 0.0075000000000000015 = <diffusion2d.SolveDiffusion2D object at 0x000002355456CB90>.dt

tests\unit\test_diffusion2d_functions.py:34: AssertionError
------------------------------------------------ Captured stdout call -------------------------------------------------
dt = 0.0075000000000000015
_____________________________________________ test_set_initial_condition ______________________________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
        solver.nx = 100
        solver.ny = 150
        solver.dx = 0.2
        solver.dy = 0.4
        solver.T_cold = 100.
        solver.T_hot = 400.

        u = solver.set_initial_condition()

>       assert u[0, 0] == solver.T_cold, "Top-left corner should be cold."
E       AssertionError: Top-left corner should be cold.
E       assert np.float64(400.0) == 100.0
E        +  where 100.0 = <diffusion2d.SolveDiffusion2D object at 0x000002355456D010>.T_cold

tests\unit\test_diffusion2d_functions.py:50: AssertionError
=============================================== short test summary info ===============================================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - AssertionError: Expected nx=150, but is 300
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters - AssertionError: Expected dt=0.0025, but is 0.0075000000000000015
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition - AssertionError: Top-left corner should be cold.
================================================== 3 failed in 0.55s ==================================================

#### intergration

================================================= test session starts =================================================
platform win32 -- Python 3.12.8, pytest-8.3.4, pluggy-1.5.0
rootdir: C:\Users\sora\Documents\Lecture\SSE\Exercise\ex6\testing-python-exercise-wt2425
collected 2 items

tests\integration\test_diffusion2d.py FF                                                                         [100%]

====================================================== FAILURES =======================================================
_________________________________________ test_initialize_physical_parameters _________________________________________

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

>       assert np.allclose(expected_dt, solver.dt), f"Expected dt={expected_dt}, but is {solver.dt}"
E       AssertionError: Expected dt=0.0025, but is 0.0075000000000000015
E       assert False
E        +  where False = <function allclose at 0x000001D317057830>(0.0025, 0.0075000000000000015)
E        +    where <function allclose at 0x000001D317057830> = np.allclose
E        +    and   0.0075000000000000015 = <diffusion2d.SolveDiffusion2D object at 0x000001D31976BFE0>.dt

tests\integration\test_diffusion2d.py:24: AssertionError
------------------------------------------------ Captured stdout call -------------------------------------------------
dt = 0.0075000000000000015
_____________________________________________ test_set_initial_condition ______________________________________________

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

>       assert np.allclose(solver_u, u), f"u should be {u},but got{solver_u}"
E       AssertionError: u should be [[100. 100. 100. ... 100. 100. 100.]
E          [100. 100. 100. ... 100. 100. 100.]
E          [100. 100. 100. ... 100. 100. 100.]
E          ...
E          [100. 100. 100. ... 100. 100. 100.]
E          [100. 100. 100. ... 100. 100. 100.]
E          [100. 100. 100. ... 100. 100. 100.]],but got[[300. 300. 300. ... 300. 300. 300.]
E          [300. 300. 300. ... 300. 300. 300.]
E          [300. 300. 300. ... 300. 300. 300.]
E          ...
E          [300. 300. 300. ... 300. 300. 300.]
E          [300. 300. 300. ... 300. 300. 300.]
E          [300. 300. 300. ... 300. 300. 300.]]
E       assert False
E        +  where False = <function allclose at 0x000001D317057830>(array([[300., 300., 300., ..., 300., 300., 300.],\n       [300., 300., 300., ..., 300., 300., 300.],\n       [300., 300....\n       [300., 300., 300., ..., 300., 300., 300.],\n       [300., 300., 300., ..., 300., 300., 300.]], shape=(150, 200)), array([[100., 100., 100., ..., 100., 100., 100.],\n       [100., 100., 100., ..., 100., 100., 100.],\n       [100., 100....\n       [100., 100., 100., ..., 100., 100., 100.],\n       [100., 100., 100., ..., 100., 100., 100.]], shape=(150, 200)))
E        +    where <function allclose at 0x000001D317057830> = np.allclose

tests\integration\test_diffusion2d.py:49: AssertionError
------------------------------------------------ Captured stdout call -------------------------------------------------
dt = 0.0075000000000000015
=============================================== short test summary info ===============================================
FAILED tests/integration/test_diffusion2d.py::test_initialize_physical_parameters - AssertionError: Expected dt=0.0025, but is 0.0075000000000000015
FAILED tests/integration/test_diffusion2d.py::test_set_initial_condition - AssertionError: u should be [[100. 100. 100. ... 100. 100. 100.]
================================================== 2 failed in 0.60s ==================================================

### unittest log

======================================================================
FAIL: test_initialize_domain (test_diffusion2d_functions.TestDiffusion2D.test_initialize_domain)
Check function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\sora\Documents\Lecture\SSE\Exercise\ex6\testing-python-exercise-wt2425\tests\unit\test_diffusion2d_functions.py", line 20, in test_initialize_domain
    self.assertEqual(solver.nx, 150, f"Expected nx=150, but got {solver.nx}")
AssertionError: 300 != 150 : Expected nx=150, but got 300

======================================================================
FAIL: test_initialize_physical_parameters (test_diffusion2d_functions.TestDiffusion2D.test_initialize_physical_parameters)
Checks function SolveDiffusion2D.initialize_domain
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\sora\Documents\Lecture\SSE\Exercise\ex6\testing-python-exercise-wt2425\tests\unit\test_diffusion2d_functions.py", line 35, in test_initialize_physical_parameters
    self.assertAlmostEqual(solver.dt, expected_dt, places=4,msg = f"Expected dt={expected_dt}, but is {solver.dt}")
AssertionError: 0.0075000000000000015 != 0.0025 within 4 places (0.005000000000000001 difference) : Expected dt=0.0025, but is 0.0075000000000000015

======================================================================
FAIL: test_set_initial_condition (test_diffusion2d_functions.TestDiffusion2D.test_set_initial_condition)
Checks function SolveDiffusion2D.get_initial_function
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\sora\Documents\Lecture\SSE\Exercise\ex6\testing-python-exercise-wt2425\tests\unit\test_diffusion2d_functions.py", line 63, in test_set_initial_condition
    self.assertAlmostEqual(solver_u[i, j], u[i, j], places=4,
AssertionError: np.float64(600.0) != np.float64(200.0) within 4 places (np.float64(400.0) difference) : u[0,0] should be 200.0,but got600.0

----------------------------------------------------------------------
Ran 3 tests in 0.004s

FAILED (failures=3)

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
