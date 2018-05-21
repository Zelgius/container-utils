# coding: utf-8
import os.path
import io
import re

from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
#README = io.open(os.path.join(here, 'README.rst'), encoding='utf8').read()
#CHANGES = io.open(os.path.join(here, 'CHANGES.txt'), encoding='utf8').read()

with io.open(os.path.join(here, 'container_utils', '__init__.py'), encoding='utf8') as version_file:
    metadata = dict(re.findall(r"""__([a-z]+)__ = "([^"]+)""", version_file.read()))

setup(
    name='container_utils',
    version=metadata['version'],
    description='A tool for packaging python libraries into containers',
    #long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD-2 License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6"
    ],
    author='Mason Egger',
    author_email='mason@masonegger.com',
    url='https://github.com/pypa/wheel',
    keywords=['cloud', 'container', 'docker'],
    license='BSD-2',
    packages=find_packages(),
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    include_package_data=True,
    zip_safe=False,
    container_options=['poo'],
    entry_points={
        'distutils.commands': [
            'bdist_container=container_utils.bdist_container:bdist_container'
            ]
        },
    extras_require={
        'container': [
            'fuck'
            ]
        },
)
