from learntools.core import binder
binder.bind(globals())
from learntools.sql.ex6 import *
print("Setup Complete")

from google.cloud import bigquery

client = bigquery.Client()

# Construct a reference to the "stackoverflow" dataset
dataset_ref = client.dataset("stackoverflow", project="bigquery-public-data")

# API request - fetch the dataset
dataset = client.get_dataset(dataset_ref)

list_of_tables = [table.table_id for table in list(client.list_tables(dataset))]

print(list_of_tables)

answers_table_ref = dataset_ref.table("posts_answers")

# API request - fetch the table
answers_table = client.get_table(answers_table_ref)

# Preview the first five lines of the "posts_answers" table
client.list_rows(answers_table, max_results=5).to_dataframe()

questions_table_ref = dataset_ref.table("posts_questions")

# API request - fetch the table
questions_table = client.get_table(questions_table_ref)

# Preview the first five lines of the "posts_questions" table
client.list_rows(questions_table, max_results=5).to_dataframe()

questions_query = """
                  SELECT id, title, owner_user_id
                  FROM `bigquery-public-data.stackoverflow.posts_questions`
                  WHERE tags LIKE '%bigquery%'
                  """


safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=10**10)
questions_query_job = client.query(questions_query, safe_config)

# API request - run the query, and return a pandas DataFrame
questions_results = questions_query_job.to_dataframe()

# Preview results
print(questions_results.head())

answers_query = """
                SELECT a.id, a.body, a.owner_user_id
                FROM `bigquery-public-data.stackoverflow.posts_questions` AS q 
                INNER JOIN `bigquery-public-data.stackoverflow.posts_answers` AS a
                    ON q.id = a.parent_id
                WHERE q.tags LIKE '%bigquery%'
                """

safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=27*10**10)
answers_query_job = client.query(answers_query, job_config=safe_config)

# API request - run the query, and return a pandas DataFrame
answers_results = answers_query_job.to_dataframe()

# Preview results
print(answers_results.head())

bigquery_experts_query = """
                         SELECT a.owner_user_id AS user_id, COUNT(1) AS number_of_answers
                         FROM `bigquery-public-data.stackoverflow.posts_questions` AS q
                         INNER JOIN `bigquery-public-data.stackoverflow.posts_answers` AS a
                             ON q.id = a.parent_Id
                         WHERE q.tags LIKE '%bigquery%'
                         GROUP BY a.owner_user_id
                         """


safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=10**10)
bigquery_experts_query_job = client.query(bigquery_experts_query, job_config=safe_config)

# API request - run the query, and return a pandas DataFrame
bigquery_experts_results = bigquery_experts_query_job.to_dataframe()

# Preview results
print(bigquery_experts_results.head())

