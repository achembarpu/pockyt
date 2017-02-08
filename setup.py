from __future__ import absolute_import, print_function, unicode_literals, with_statement

import sys
from setuptools import setup, find_packages


if sys.version_info[0:2] not in ((2, 7), (3, 4), (3, 5), (3, 6)):
    print('This version of Python is unsupported !\n'
          'Please use Python 2.7.x, 3.4.x, 3.5.x, or 3.6.x !')
    sys.exit(1)


name = 'pockyt'
version = '1.1'
motto = 'automate and manage your pocket collection'
author = 'Arvind Chembarpu'
email = 'achembarpu@gmail.com'
github = 'https://github.com/arvindch'

try:
    with open('README.rst') as f:
        description = f.read()
except:
    description = ''

setup(
    name=name,
    packages=find_packages(),
    version=version,
    description=motto,
    long_description=description,
    author=author,
    author_email=email,
    url='{}/{}'.format(github, name),
    license='GPLv3+',
    install_requires=[
        'requests>=2.13',
        'parse>=1.6',
    ],
    download_url='{}/{}/tarball/{}'.format(github, name, version),
    keywords=['pocket', 'commandline', 'automation'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Topic :: Utilities',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={
        'console_scripts': [
            'pockyt=pockyt.pockyt:main',
        ],
    },
)
