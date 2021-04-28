# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/01_analysis.ipynb (unless otherwise specified).

__all__ = ['find_max_nonzero', 'find_range', 'get_edep_data', 'get_df_subentry2']

# Cell
import pandas as pd
import uproot as rt
import awkward as ak

from scipy.stats import moyal
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import stats
from scipy.stats import rv_continuous
# import pylandau
from matplotlib.pyplot import hist2d
import matplotlib.colors as mcolors

# Cell
def find_max_nonzero(array_hist):
    """returns an upper boundary of the continuos non-zero bins

    input a histogram array output from plt.hist
    """
    previous = -1
    preprevious  = -1
    p_b = -1
    pp_b = -1
    for v, b in zip(array_hist[0],array_hist[1]):
        if preprevious != 0 and previous == 0 and v == 0:
            return math.ceil(p_b)
        pp_b = p_b
        p_b = b
        preprevious = previous
        previous = v


# Cell
def find_range(param):
    """removes a tail in the upper range of the histogram"""
    array_hist = plt.hist(param, bins=100)
    upper_limit = find_max_nonzero(array_hist)
    ret = -1
    while upper_limit:
        ret = upper_limit
        array_hist = plt.hist(param[param < upper_limit], bins=100)
        upper_limit = find_max_nonzero(array_hist)
    return ret

# Cell
def get_edep_data(df, sensor=-1):
    """returns an array of energies deposited in each event (keV)"""



    # sum all energy deposited in each event and convert the result to keV
    if sensor == -1:
        edep = df.groupby(['eventID'])['edep'].sum()*1000
    else:
        edep = (df[df['volumeID'] == sensor].groupby(['eventID']))['edep'].sum()*1000
    return edep

# Cell
def get_df_subentry2(root_file_name):
    """returns a dataframe that contains only subentry 2 data

    This subentry seems to contain all the relevant information"""

    df = pd.DataFrame()
    with rt.open(f'{root_file_name}:Hits') as tree:
        df = ak.to_pandas(tree.arrays())
    return df.xs(2, level='subentry')