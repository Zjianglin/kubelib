# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

os.chdir(os.path.dirname(__file__))
with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='kubelib',
    version='0.0.1',
    description='Utility wrapper around Kubectl',
    long_description=readme,
    author='Jason Kane',
    author_email='jkane@safaribooksonline.com',
    url='https://safaribooks.com',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        'bunch',
        'PyYaml',
        'sh',
        'glob2',
    ],
    entry_points={
        'console_scripts': [
            'make_namespace=kubelib.cli:make_namespace',
            'make_nodeport=kubelib.cli:make_nodeport',
        ]
    }
)
