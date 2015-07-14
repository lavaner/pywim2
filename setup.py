# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from os import path

setup(
    name='pyWIM2',
    version='0.1',
    description='A python version of WINNER II Channel Model',
    long_description='',
    url='https://github.com/lavaner/pywim2',
    author='liuyuan',
    author_email='lavaner@sina.com',
    license='GPL',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Programing Language :: Python :: 2',
        'Programing Language :: Python :: 2.7',
        'Programing Language :: Python :: 3',
        'Programing Language :: Python :: 3.4'
    ],

    keywords='system and/or link simulation channel model',
    install_requires=['numpy'],
    extras_require={
        'dev': ['check-manifest'],
        'test' : ['nose','coverage'],
    },
)
