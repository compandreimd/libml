from setuptools import setup, find_packages

setup(
    name="libml",
    version="0.0.1",
    author="compandreimd",
    author_email="compandreimd@gmail.com",
    url="https://github.com/compandreimd/libml",
    description="Description of ML download content",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    entry_points={"console_scripts": ["libml = libml.main:download"]},
)
 