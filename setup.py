from __future__ import absolute_import, print_function, unicode_literals, with_statement

import sys
from setuptools import setup, find_packages

if sys.version_info[0:2] not in ((2, 7), (3, 4), (3, 5), (3, 6)):
    print('This version of Python [%s] is unsupported !\n'
          'Please use Python 2.7.x, 3.4.x, 3.5.x, or 3.6.x !'
          % ('.'.join(str(i) for i in sys.version_info[0:3])))
    sys.exit(1)


name = 'pockyt'
version = '1.1'
motto = 'automate and manage your pocket collection'
author = 'Arvind Chembarpu'
email = 'achembarpu@gmail.com'
github = 'https://github.com/arvindch/%s' % (name)

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
    url=github,
    license='GPLv3+',
    install_requires=[
        'parse>=1.6',
    ],
    download_url='%s/tarball/%s' % (github, version),
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
