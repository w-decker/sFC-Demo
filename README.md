# sFC-Demo

This repository includes code to calculate static functional connectivity (sFC) from functional magnetic resonance imaging (fMRI) data. 

## Files

[`main.ipynb`](/main.ipynb) - Step-by-step deployment of code.

[`utils.py`](/utils.py) - Utilities needed for sFC execution. Includes custom built functionality in the form of `FuncData`, a class to create two-dimensional data with embedded correlations of one's choice. Also contains functions for data I/O.

## Dependencies

This code relies on the `nilearn.connectome` submodule. Installation and/or usage instructions can be found [here](https://nilearn.github.io/stable/index.html).

## Using this repo

A conda environment, `sfc-demo`, has been created specifically for this repository.

To use this repository, first clone it.

```bash
git clone https://github.com/w-decker/sFC-Demo.git
cd sFC-Demo
```

Next, activate the conda environment.

```bash
conda create -f environment.yml
conda activate sfc-demo
```




