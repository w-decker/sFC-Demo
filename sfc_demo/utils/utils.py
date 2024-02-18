import numpy as np
from collections import Counter
from nilearn.datasets import fetch_development_fmri
import deepdish as dd
import os
import wget

def nilearn_io():
    """Load in prespecified nilearn dataset
    
    Return
    ------
    data: Bunch
    """

    # get data
    D = fetch_development_fmri(n_subjects=10, age_group='adult', verbose=True)

    return D

def sherlock_io():
    """Load in sherlock dataset
    
    Return
    ------
    data
    """
    
    # make data directory
    data_dir = os.mkdir('sherlock_data')
    data_path = os.path.join(os.getcwd(), data_dir)

    # sherlock data URLs
    url_sherlock = 'https://ndownloader.figshare.com/files/9017983'

    # download data
    wget.download(url_sherlock, out=os.path.join(data_path, 'sherlock.h5'))

    # check
    if os.path.exists(os.path.join(data_path, 'sherlock.h5')):
        print(f'Successful download in \t {data_path}')

    else:
        print(f'Failed to download in \t {data_path}')

    # load data
    D = dd.io.load(os.path.join(data_path, f'sherlock.h5'))

    return D

def data_io(data: str):
    """fMRI data I/O
    
    Parameters
    ----------
    data: str
        Which data do you want to load?
        If 'help' is passed as arg, output is list of different data options
        
    Return
    ------
    data: np.ndarray
    
    """

    # check is someone needs help
    if data is 'help':
        print(f"Data category:\t'corresponding argument'")
        print('----------------------------------------')
        print(f"Nilearn:\t'nilearn'")
        print(f'\t\tLoads in nilearn dataset')
        print()
        print(f"Sherlock:\t'sherlock'")
        print(f'\t\tLoads sherlock dataset from Chen et al. (2017)')
        print()
    elif data is 'nilearn':
        D = nilearn_io()

    elif data is 'sherlock':
        D = sherlock_io()

    return D

def get_voxel_pairs(data: np.ndarray, n_corrs: int) -> list[tuple] | Counter:
    """Get voxel pairs
    
    Parameters
    ----------
    data: np.ndarray
        Voxel x Time matrix

    Return
    ------
    labels: list[tuple]
        List of voxel pairs

    voxel_counter: Counter
        Track single voxel usage occurances
    """

    # Hold voxel pairs
    labels = []

    # track single voxel occurances
    voxel_counter = Counter()

    while len(labels) < n_corrs:
        idx = tuple(sorted(np.random.choice(data.shape[0], size=2, replace=False)))
        if all(voxel_counter[i] == 0 for i in idx):
            labels.append(idx)
            voxel_counter.update(idx)

    return labels, voxel_counter
