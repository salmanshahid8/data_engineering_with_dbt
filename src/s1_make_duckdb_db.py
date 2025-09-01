import duckdb

sql_query = '''show tables'''

with duckdb.connect("data/nyc_parking_violations.db") as con:
    print(con.sql(sql_query).df())