from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize("prime_numbers_cy.pyx"))
