from dataclasses import dataclass
import numpy as np
from utils import get_voxel_pairs

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





