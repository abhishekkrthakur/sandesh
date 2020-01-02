from setuptools import setup, Extension
from setuptools import find_packages

import sandesh

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

if __name__ == "__main__":
    setup(
        name="sandesh",
        version=sandesh.__version__,
        description="sandesh - a simple app to send messages on slack",
        long_description=long_description,
        long_description_content_type='text/markdown',
        author="Abhishek Thakur",
        author_email="abhishek4@gmail.com",
        url="https://github.com/abhishekkrthakur/sandesh",
        license="MIT License",
        packages=find_packages(),
        include_package_data=True,
        platforms=["linux", "unix"],
        python_requires='>3.5.2'
    )
