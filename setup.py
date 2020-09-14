# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 14:39:13 2020

@author: rhs
"""
#https://packaging.python.org/tutorials/packaging-projects/
#https://packaging.python.org/guides/distributing-packages-using-setuptools/#package-data

import setuptools

with open('requirements.txt') as requirements:
    required = requirements.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="facebookScraper", 
    version="0.1.4",
    author="Rasmus H. Schmøkel",
    author_email="rasmusschmokel@gmail.com",
    description="A python module for scraping facebook",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires = required,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        'Development Status :: 3 - Alpha'
    ],
    python_requires='==3.7.*',
    entry_points={
        "console_scripts": [
            "facebookScraper = facebookScraper.cli:main"
        ]
    }
)

# RUN 'python3 setup.py sdist bdist_wheel' in cmd to create built dist and source dist