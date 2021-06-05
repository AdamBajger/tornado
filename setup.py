#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup

setup(
    name="alipesa_tornado",
    version='1.0.0',
    description="Tornado Framework",
    long_description="",
    classifiers=[],
    author="Ali Pesaranghader",
    
    url="https://github.com/alipsgh/tornado",
    license="MIT",
    packages=["archiver", "classifier", "data_structures",
              "dictionary", "drift_detection", "evaluators",
              "filters", "graphic", "plotter", "streams.generators",
              "streams.readers", "tasks"],
    package_dir={"alipesa_tornado": "."},
    include_package_data=True,
    zip_safe=True,
    setup_requires=[
        "setuptools",
    ],
    install_requires=[
        "numpy"
        "oauth2client",
        "google",
        "tqdm",
        "ijson",
        "ipython",
    ],
    package_data={"alipesa_tornado": ["data_streams/*"]},
)

# vim: set cin et ts=4 sw=4 ft=python :11
