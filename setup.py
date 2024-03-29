# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 14:39:13 2020

@author: rhs
"""


import setuptools

with open('requirements.txt') as requirements:
    required = requirements.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fbadlibrarian", 
    version="0.2.2",
    author="Rasmus Schmøkel",
    author_email="rasmusschmokel@gmail.com",
    description="A helpful librarian for the Facebook AdLibrary",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires = required,
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        'Development Status :: 3 - Alpha'
    ],
    python_requires='==3.10.*',
    entry_points={
        "console_scripts": [
            "FBAL = FBAdLibrarian.cli:main"
        ]
    }
)

# RUN 'python3 setup.py sdist bdist_wheel' in cmd to create built dist and source dist