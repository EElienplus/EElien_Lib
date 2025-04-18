from setuptools import setup, find_packages

setup(
    name = 'EElienLib',
    version = '0.1',
    packages = find_packages(),
    install_requires = [
        'pillow',
        'beautifulsoup4',
        'requests'
    ],

)