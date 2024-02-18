from setuptools import setup, find_packages

setup(
    name="sfc-demo",
    version="0.0.1",
    author="Will Decker",
    author_email="deckerwill7@gmail.com",
    description="Tools for executing static functional connectivity analysis",
    url="https://github.com/w-decker/sfc-demo/tree/main/sfc-demo",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering"
    ],
    python_requires='>=3.8'
)