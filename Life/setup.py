from setuptools import setup, find_packages
import codecs
import os
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

VERSION = '0.0.3'
DESCRIPTION = 'Conway\'s Game of Life.'
LONG_DESCRIPTION = 'Life is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves.'

# Setting up
setup(
    name="conway-life-game",
    version=VERSION,
    author="Gabriel Braden",
    author_email="<gbrad012@uottawa.ca>",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown", 
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
