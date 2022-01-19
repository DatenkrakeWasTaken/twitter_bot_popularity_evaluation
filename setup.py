#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Maximilian Pekarski",
    author_email='maximilian.pekarski@gmail.com',
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
    description="Twitter bot for evaluating popularity of two different topics, in this case cats and dogs.[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[D[C[C: cats and dogs.",
    entry_points={
        'console_scripts': [
            'twitter_bot_popularity_evaluation=twitter_bot_popularity_evaluation.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='twitter_bot_popularity_evaluation',
    name='twitter_bot_popularity_evaluation',
    packages=find_packages(include=['twitter_bot_popularity_evaluation', 'twitter_bot_popularity_evaluation.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/DatenkrakeWasTaken/twitter_bot_popularity_evaluation',
    version='0.1.0',
    zip_safe=False,
)
