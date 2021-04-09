# AUTOGENERATED! DO NOT EDIT! File to edit: 01_analysis.ipynb (unless otherwise specified).

__all__ = ['get_edep_data']

# Cell
import uproot as rt
from scipy.stats import moyal
import awkward as ak
import pandas as pd

def get_edep_data(root_file_name):
    edep = pd.Series(dtype='float64')
    with rt.open(root_file_name) as root_file:
        tree = root_file['Hits;11']
        df = ak.to_pandas(tree.arrays())
        df_vID3 = df[df.volumeID == 3]
        edep = df_vID3.groupby(['eventID'])['edep'].sum()*1000
    return edep