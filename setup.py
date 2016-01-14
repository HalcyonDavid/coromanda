try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from validate import __version__


setup(
    name = 'coromanda',
    version = __version__,
    author = 'David',
    author_email = 'davidwfallis@googlemail.com',
    packages = ['coromanda'],
    include_package_data = True,
    scripts = ['bin/update', 'bin/coro'],
    url = '',
    description = 'Game prediction',
    long_description = 'Game prediction',
    install_requires = [
        'sqlalchemy',
        'numpy >=1.9.2',
        'matplotlib >=1.4.3',
        'pyyaml >=3.11',
    ],
)
