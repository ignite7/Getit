""" Setup of the module 'setup.py' which will
install all the requirements of the program.
"""

# Libraries imported
from setuptools import setup, find_packages
from os import path, system


# Requires
install_requires_file = open('./setup/requirements.txt', 'r+').read().splitlines()


# Adsolute path
here = path.abspath(path.dirname(__file__))


# Long description from README.md file
with open(path.join(here, 'README.md'), encoding = 'utf-8') as readme:
    long_description = readme.read()


# Specifications of the setup
setup(
    name = 'Getit',
    version = '1.0',
    description = 'Get anything from URL to your computer!',
    long_description = long_description,
    url = 'https://sergiovanberkel.com/',
    author = 'Sergio van Berkel Acosta',
    author_mail = 'sergio.vanberkel@gmail.com',
    packages = find_packages(),
    python_requires = '>=3.5.*',
    install_requires = install_requires_file or system('pip install -r ./setup/requirements.txt')
)