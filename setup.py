from setuptools import setup
from setuptools import find_packages

setup(
    name='ihme_math_utils',
    version='0.0.0',
    description='Math and Stat utilities for IHME',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'scikit-learn',
        'numpy',
        'pandas',
        'scipy'
    ],
    zip_safe=False,
)

