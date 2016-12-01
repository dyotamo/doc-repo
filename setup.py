#!/usr/bin/env python

from setuptools import setup

setup(
    # GETTING-STARTED: set your app name:
    name='Neodoli',
    # GETTING-STARTED: set your app version:
    version='1.0',
    # GETTING-STARTED: set your app description:
    description='Find pharmacies, clinics and labs near by you',
    # GETTING-STARTED: set author name (your name):
    author='Dássone Yotamo (Neodoli)',
    # GETTING-STARTED: set author email (your email):
    author_email='dyotamo@gmail.com',
    # GETTING-STARTED: set author url (your url):
    url='http://www.python.org/sigs/distutils-sig/',
    # GETTING-STARTED: define required django version:
    install_requires=[
        'Django==1.8.4',
        'Djangorestframework==3.4.7',
        'Django-jet==1.0.3',
        'PyMySQL==0.6.7',
        'Pillow==2.7.0',
        'Django-filter==1.0.1',
    ],
    dependency_links=[
        'https://pypi.python.org/simple/django/'
    ],
)
