from setuptools import setup

setup(
    name = 'Getit',
    version = '1.0',
    py_modules = ['main'],
    install_requires = [
        'Pillow',
        'pytube3',
        'urllib3'
    ]
)