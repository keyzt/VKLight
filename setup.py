#!/usr/bin/env python

import os
import re

from setuptools import setup, find_packages


def get_version(file_rel_path):
    base_dir = os.path.dirname(__file__)
    file_abs_path = os.path.join(base_dir, file_rel_path)
    with open(file_abs_path) as file:
        file_content = file.read()
        version = re.findall(r"^__version__ = '(.+)'$", file_content, re.MULTILINE)[0]
        return version


setup(
    name='VKLight',
    version='1.1',
    author='Ivan',
    author_email='',

    url='https://github.com/keyzt/VKLight',
    download_url='https://github.com/keyzt/VKLight/archive/master.zip',
    description='Light wrapper for VK\'s API',

    packages=find_packages(),
    install_requires=[
        'requests',
    ],

    license='MIT License',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    keywords='vk.com vk api vk_api',
)