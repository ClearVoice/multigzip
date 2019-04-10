from setuptools import setup

from multigzip import __version__

setup(
    name='multigzip',
    version=__version__,
    provides=['multigzip'],
    author='Jeff Nappi',
    url='https://github.com/jeffnappi/multigzip',
    setup_requires='setuptools',
    license='MIT',
    author_email='jeff@clearvoice.com',
    description='Multi Member GZip Support for Python 3',
    packages=['multigzip']
)
