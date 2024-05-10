from learntools.core import binder
binder.bind(globals())
from learntools.data_cleaning.ex4 import *

import pandas as pd
import numpy as np

# helpful character encoding module
import charset_normalizer


# set seed for reproducibility
np.random.seed(0)

sample_entry = b'\xa7A\xa6n'
print(sample_entry)
print('data type:', type(sample_entry))

new_entry = sample_entry.decode("big5-tw", errors="replace")
new_entry = new_entry.encode("utf-8", errors="replace")
print(type(new_entry))

police_killings = pd.read_csv("../input/fatal-police-shootings-in-the-us/PoliceKillingsUS.csv", encoding='Windows-1252')

police_killings.to_csv('police_killings_records.csv')

