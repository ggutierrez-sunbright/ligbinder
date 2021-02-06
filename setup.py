#!/usr/bin/env python

from setuptools import setup

setup(
    name='LigBinder',
    version='0.1',
    description='automatic targeted molecular dynamics for ligand bindning',
    author='Guillermo Gutierrez',
    author_email='',
    url='',
    packages=['ligbinder', 'ligbinder.data'],
    # as an example of additional data:
    inlcude_package_data=True,
    data_files=[("ligbinder",["ligbinder/data/default_config.yml"])],
    scripts=['bin/ligbinder'],
    #install_requires=["pytraj>=2"]
)
