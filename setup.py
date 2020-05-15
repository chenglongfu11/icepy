#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: clong
# Mail: fuc369702700@gmail.com
# Created Time:  2020-5-7
# Last Update: 2020-5-15
#############################################


from setuptools import setup, find_packages

setup(
    name = "icepy",
    version = "0.0.2",
    keywords = ("pip", "pathtool","timetool", "magetool", "mage"),
    description = "automated simulation tool for IDA ICE 4.8",
    long_description = "automated simulation tool for IDA ICE 4.8 Updated on 5/15/2020",
    license = "MIT Licence",

    url = "https://github.com/chenglongfu11/icepy",
    author = "Clong",
    author_email = "fuc369702700@gmail.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = []
)
