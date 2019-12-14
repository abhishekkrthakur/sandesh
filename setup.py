from setuptools import setup, Extension
from setuptools import find_packages

import sandesh

if __name__ == "__main__":
    setup(
        name="sandesh",
        version=sandesh.__version__,
        description="sandesh - a simple app to send messages on slack",
        author="Abhishek Thakur",
        license="MIT License",
        packages=find_packages(),
        include_package_data=True,
        platforms=["linux", "unix"],
        python_requires='>3.5.2'
    )
