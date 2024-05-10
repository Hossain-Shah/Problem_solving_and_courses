import pandas as pd
pd.set_option("display.max_rows", 5)
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

from learntools.core import binder; binder.bind(globals())
from learntools.pandas.summary_functions_and_maps import *
print("Setup complete.")

reviews.head()

median_points = reviews.points.median()

countries = reviews.country.unique()

reviews_per_country = reviews.country.value_counts()

centered_price = reviews.price - reviews.price.mean()

bargain_wine = reviews.loc[(reviews.points / reviews.price).idxmax(), 'title']

descriptor_counts = pd.Series([reviews.description.map(lambda desc: "tropical" in desc).sum(), reviews.description.map(lambda desc: "fruity" in desc).sum()], index=['tropical', 'fruity'])

def stars(row):
    if row.country == 'Canada':
        return 3
    elif row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1

star_ratings = reviews.apply(stars, axis='columns')

