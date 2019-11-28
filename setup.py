# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
from setuptools import setup, find_packages, Command
from setuptools.command.test import test as TestCommand
import sys


pkgmeta = {}
pkgmeta_path = os.path.join(os.path.dirname(__file__), 'memcachedkeys', 'pkgmeta.py')
with open(pkgmeta_path) as f:
    code = compile(f.read(), pkgmeta_path, 'exec')
    exec(code, pkgmeta)

class LintCommand(Command):
    """
    A copy of flake8's Flake8Command

    """
    description = "Run flake8 on modules registered in setuptools"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def distribution_files(self):
        if self.distribution.packages:
            for package in self.distribution.packages:
                yield package.replace(".", os.path.sep)

        if self.distribution.py_modules:
            for filename in self.distribution.py_modules:
                yield "%s.py" % filename


readme = open('README.rst').read()

setup(
    name=pkgmeta['__title__'],
    version=pkgmeta['__version__'],
    description='Sanitize your keys, please.',
    long_description=readme,
    author=pkgmeta['__author__'],
    author_email='m@tthewwithanm.com',
    url='https://github.com/hzdg/django-memcachedkeys',
    packages=find_packages(),
    include_package_data=True,
    setup_requires=[
        'flake8',
    ],
    install_requires=[
        'Django>=1.11',
    ],
    zip_safe=False,
    keywords='django-memcachedkeys',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    cmdclass={
        'lint': LintCommand,
    },
)
