#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: clong
# Mail: fuc369702700@gmail.com
# Created Time:  2020-5-7
# Last Update: 2020-7-21
#############################################


from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        README = f.read()
    return README    


setup(
    name = "icepy",
    version = "0.0.7",
    description = "Automated simulation tool for IDA ICE",
    long_description = readme(),
    long_description_content_type = "text/markdown",
    license = "MIT Licence",
    classifiers = [
        "Programming Language :: Python :: 3"
    ],
    url = "https://github.com/chenglongfu11/icepy",
    author = "Clong",
    author_email = "fuc369702700@gmail.com",

    packages = ["icepy", "icepy.zonestructure"],
    include_package_data = True,
    platforms = "any",
    install_requires = ["pandas", "plotly", "pymysql", "beautifulsoup4", "numpy"],
    entry_points={
        "console_script":[
            "icepy=icepy.modeleditor"
        ]
    }
)
