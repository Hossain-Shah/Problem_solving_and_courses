from learntools.core import binder
binder.bind(globals())
from learntools.sql.ex1 import *
from google.cloud import bigquery


# Create a "Client" object
client = bigquery.Client()

# Construct a reference to the "chicago_crime" dataset
dataset_ref = client.dataset("chicago_crime", project="bigquery-public-data")

# API request - fetch the dataset
dataset = client.get_dataset(dataset_ref)

tables = list(client.list_tables(dataset))


# Print names of all tables in the dataset (there are four!)
for table in tables:  
    print(table.table_id)

num_tables = 1

client.list_rows(table, max_results=5).to_dataframe()

num_timestamp_fields = 2

fields_for_plotting = ['latitude', 'longitude']

