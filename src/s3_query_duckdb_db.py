import duckdb
from pprint import pprint

sql_query = '''SELECT * FROM first_model LIMIT 5'''

with duckdb.connect("data/nyc_parking_violations.db") as con:
    df = con.sql(sql_query).df()

pprint(df)