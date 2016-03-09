# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='data-structures',
    description='A collection of classic data structures',
    version=0.1,
    author='Paul Sheirdan and Adam Palmer',
    author_email='paul.sheridan@me.com and apalm112@gmail.com',
    license='MIT',
    py_modules=['linked_list', 'stack', 'double_linked'],
    package_dir={'': 'src'},
    extras_require={'test': ['pytest', 'pytest-xdist', 'tox']},
)
