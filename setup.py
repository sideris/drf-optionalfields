from setuptools import setup


classifiers = [
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Topic :: Software Development :: Libraries",
    "Intended Audience :: Developers",
    "Framework :: Django",
]

with open("README.rst") as f:
    long_description = f.read()

setup(
    name="drf-optionalfields",
    version="1.0.0",
    description="Get fields only when you need them",
    long_description=long_description,
    packages=["drf_optionalfields"],
    author="Petros G. Sideris",
    author_email="pgsideris@gmail.com",
    license="MIT",
    url="https://github.com/sideris/drf-optionalfields",
    classifiers=classifiers,
    extras_require={
        "dev": [
            "pytest", "pytest-cov", "pytest-django", "coveralls",
            "django", "djangorestframework", "mock_django",
            "setuptools", "wheel",
        ]
    },
)
