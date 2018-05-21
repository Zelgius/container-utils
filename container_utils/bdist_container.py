"""
Create a containerized deployment of a Python package/application.
"""

import csv
import hashlib
import os
import subprocess
import shutil
import sys
import re
from distutils.core import Command
from distutils.sysconfig import get_python_version
from distutils import log as logger
from shutil import rmtree

import pkg_resources


safe_name = pkg_resources.safe_name
safe_version = pkg_resources.safe_version


def safer_name(name):
    return safe_name(name).replace('-', '_')


def safer_version(version):
    return safe_version(version).replace('-', '_')


class bdist_container(Command):

    description = 'create a container distribution'

    user_options = [('hello=', None,
                     "hello bdist"),
                   ]

    def initialize_options(self):
        self.hello = None
        print(vars(self.distribution))

    def finalize_options(self):
        print('worse error handling')

    def run(self):
        if self.hello is None:
            print('hello')
        else:
            print(self.hello)
