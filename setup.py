#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=7.0',
    'certifi>=14.05.14',
    'six>=1.10',
    'python_dateutil>=2.5.3',
    'setuptools>=21.0.0',
    'urllib3>=1.15.1'
]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Dmitry Kozhedubov",
    author_email='hiisi13@gmail.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Python клиент для API распознавания и синтеза речи Облака ЦРТ",
    entry_points={
        'console_scripts': [
            'speechpro=speechpro.cli:cli',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='speechpro',
    name='speechpro-cloud-python',
    packages=find_packages(include=['speechpro', 'speechpro.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/speechpro/cloud-python',
    version='0.1.7',
    zip_safe=False,
)
