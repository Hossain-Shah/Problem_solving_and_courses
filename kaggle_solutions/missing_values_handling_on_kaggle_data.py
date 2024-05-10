from learntools.core import binder
binder.bind(globals())
from learntools.data_cleaning.ex1 import *

import pandas as pd
import numpy as np


# read in all our data
sf_permits = pd.read_csv("../input/building-permit-applications-data/Building_Permits.csv")

# set seed for reproducibility
np.random.seed(0)

sf_permits.head(5)

percent_missing = (sf_permits.isnull().sum().sum()/ np.product(sf_permits.shape)) * 100

sf_permits.dropna().shape[1]

sf_permits_with_na_dropped = sf_permits.dropna(axis=1)

dropped_columns = sf_permits.shape[1]-sf_permits_with_na_dropped.shape[1]

sf_permits_with_na_imputed = sf_permits.fillna(method='bfill', axis=0).fillna(0)

