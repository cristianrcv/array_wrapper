from distutils.core import setup
from Cython.Build import cythonize

setup(
        ext_modules=cythonize("src/array_wrapper.pyx"),
)
