from codecs import open
from os.path import abspath, dirname, join , expanduser

from setuptools import Command, find_packages, setup

from instagram_py import __version__


this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.rst'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name = 'instagram-py',
    version = __version__,
    description = 'A python script to execute brute force attack on Instagram',
    long_description = long_description,
    url = 'https://github.com/DeathSec/Instagram-Py',
    download_url = 'https://github.com/deathsec/instagram-py/archive/v'+str(__version__)+'.tar.gz',
    author = 'DeathSec',
    author_email = 'antonyjr@protonmail.com',
    license = 'MIT',
    classifiers = [
        'Topic :: Utilities',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.6'
    ],
    keywords = ['cli' , 'hack' , 'instagram' , 'with' , 'out' , 'password' , 'limit' , 'brute' ,
                'force' , 'attack' , 'instagram'],
    packages = find_packages(exclude=['docs', 'tests*']),
    install_requires = ['requests' , 'requests[socks]' , 'stem'],
    entry_points = {
        'console_scripts': [
            'instagram-py=instagram_py:main',
        ],
    },

)
