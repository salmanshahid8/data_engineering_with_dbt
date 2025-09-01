import duckdb
from pprint import pprint

sql_query = '''SELECT * FROM parking_violations_2023 LIMIT 5'''

with duckdb.connect("data/nyc_parking_violations.db") as con:
    df = con.sql(sql_query).df()

pprint(df)