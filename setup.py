from setuptools import Extension, setup
from Cython.Build import cythonize
import numpy as np

extensions = [
    Extension(
        "orthogonal_matching_pursuit_gpu.blas_kernels._kernels",
        ["src/orthogonal_matching_pursuit_gpu/blas_kernels/_kernels.pyx"],
        include_dirs=[np.get_include()],
    )
]

setup(
    ext_modules=cythonize(
        extensions,
        language_level="3",
    ),
)
