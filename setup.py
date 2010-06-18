# -*- coding: utf-8 -*-
#
# © 2010 SimpleGeo, Inc. All rights reserved.
# Author: Ben Standefer <benstandefer@gmail.com>
#

from setuptools import setup, find_packages

setup(name="python-hbase",
      version='0.20.4',
      description="Thrift client for HBase",
      url="http://hbase.apache.org/",
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      author="Ben Standefer",
      author_email="benstandefer@gmail.com",
      scripts=['scripts/Hbase-remote'],
      keywords="database hbase hadoop",
      install_requires=['Thrift'])
