import setuptools

requires = [
    'isort',
    'flake8>=3.0.0',
]

setuptools.setup(
    name="flake8_imports",
    license="MIT",
    version="0.1.0",
    description="isort extension flake8",
    author="Michael van Tellingen",
    author_email="michaelvantellingen@gmail.com",
    url="https://gitlab.com/mvantellingen/flake8-imports",
    install_requires=requires,
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
