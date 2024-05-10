from learntools.core import binder
binder.bind(globals())
from learntools.data_cleaning.ex3 import *

import pandas as pd
import numpy as np
import seaborn as sns
import datetime


# read in our data
earthquakes = pd.read_csv("../input/earthquake-database/database.csv")

# set seed for reproducibility
np.random.seed(0)

earthquakes.head()
earthquakes['Date'].dtype

earthquakes[3378:3383]

date_lengths = earthquakes.Date.str.len()
date_lengths.value_counts()

indices = np.where([date_lengths == 24])[1]
print('Indices with corrupted data:', indices)
earthquakes.loc[indices]

earthquakes['date_parsed'] = pd.to_datetime(earthquakes['Date'], format="%m/%d/%Y")

day_of_month_earthquakes = earthquakes['date_parsed'].dt.day

day_of_month_earthquakes = day_of_month_earthquakes.dropna()

# plot the day of the month
sns.displot(day_of_month_earthquakes, kde=False, bins=31)

volcanos = pd.read_csv("../input/volcanic-eruptions/database.csv")

volcanos['Last Known Eruption'].sample(5)