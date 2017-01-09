#! /usr/bin/env python
# vim: set fileencoding=utf-8

from setuptools import setup


setup(
    name="pymnet",
    version="0.1",
    description="Library for analysing multilayer networks",
    url="https://bitbucket.org/bolozna/multilayer-networks-library",
    author="Mikko Kivelä",
    author_email="mikko.kivela@iki.fi",
    packages=["pymnet", "pymnet.tests"]
)