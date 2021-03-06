#!/usr/bin/env python
from distutils.core import setup

setup(
    name='django_sane_reverse',
    version=1.0,
    author='Raphael Kimmig',
    author_email='raphael.kimmig@ampad.de',
    url = 'https://github.com/RaphaelKimmig/django_sane_reverse',

    description = 'Sane reverse function for django urls',

    license = 'BSD',
    packages=['django_sane_reverse'],
    requires = ['django (>=1.2)'],

    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
    ],
)
