#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

setup(
    name='django-delegated-auth',
    version='0.1.0',
    description='An authentication backend that looks at another Django application',
    author='John Goodleaf',
    author_email='jgoodleaf@stadi.us',
    url='http://github.com/toastdriven/django-tastypie/',
    long_description=open('README.rst', 'r').read(),
    packages=[
        'delegated-auth',
    ],
    package_data={
        'tastypie': ['templates/tastypie/*'],
    },
    zip_safe=False,
    requires=[
        'django',
        'ez_setup',
        ],
    install_requires=[
        'django',
        'ez_setup',
    ],
    classifiers=[
        'Development Status :: 3 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
)