#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'loguru',
    'redis'
]

test_requirements = [ ]

setup(
    author="Sam Texas",
    author_email='github@simplecto.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A robust and scalable API client to crawl github politely and within the limits",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='github_api_crawler',
    name='github-api-crawler',
    packages=find_packages(include=['github_api_crawler', 'github_api_crawler.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/Carabinr/github-api-crawler',
    version='0.1.1',
    zip_safe=False,
)
