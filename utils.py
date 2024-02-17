import numpy as np
from collections import Counter
from dataclasses import dataclass

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

@dataclass
class FuncData(object):
    """Generate faux timeseries with embedded correlations
    
    Parameters
    ----------
    size: tuple
        Voxel x Time tuple
        Each voxel represents a "region of interest (ROI)"

    n_corrs: int
        Number of correlations to create

    pearsons_r: List[int]
        Ground truth correlations to use

    """

    # get some values 
    size: tuple
    n_corrs: int
    pearsons_r: list[int]

    def create_data(self):
        """Method to make data
        
        Returns
        -------
        X: numpy.ndarray
            Voxel x Time matrix
        """
        
        # empty data matrix
        X = np.random.uniform(size=self.size, low=0.1, high=0.99)

        # get which voxels to correlate
        self.vox_pairs, _ = get_voxel_pairs(data=X, n_corrs=self.n_corrs)

        # track correlations of voxels
        self.voxel_info = {key: None for key in self.vox_pairs}

        # make covariance matrix
        for _, k, j in zip(range(self.n_corrs), self.pearsons_r, self.vox_pairs):

            # make correlations
            cov_matrix = np.array([[1, k], [k, 1]])
            c = np.random.multivariate_normal(mean=[0, 0], cov=cov_matrix, size=X.shape[1]).T

            # put back into data
            X[j[0]] = c[0]
            X[j[1]] = c[1]

            self.voxel_info[j] = k

        self.data = X

        return self





