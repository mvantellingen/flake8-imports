import re

import setuptools

requires = [
    'isort',
    'flake8>=3.0.0',
]

with open('README.rst') as fh:
    long_description = re.sub(
        '^.. start-no-pypi.*^.. end-no-pypi', '', fh.read(), flags=re.M | re.S)

setuptools.setup(
    name="flake8_imports",
    license="MIT",
    version="0.1.1",
    description="isort extension flake8",
    long_description=long_description,
    author="Michael van Tellingen",
    author_email="michaelvantellingen@gmail.com",
    url="https://gitlab.com/mvantellingen/flake8-imports",
    install_requires=requires,
    package_dir={'': 'src'},
    py_modules=['flake8_imports'],
    entry_points={
        'flake8.extension': [
            'I0 = flake8_imports:ImportsPlugin',
        ],
    },
    classifiers=[
        "Framework :: Flake8",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
)
