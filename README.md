# data_engineering_with_dbt
data engineering with dbt course on linkedin learning

## Steps to follow
1. Install the dependencies in an evironment. Dependencies are given in `requirements.txt`
2. make a duckdb database by executing `src/s1_make_duckdb_db.py`
3. copy data from csv to duckdb database tables by executing `src/s2_copy_data_csv_to_duckdb.py`
4. check if the data is copied by querying the database by executing `src/s3_query_duckdb_db.py`
5. create a dbt project. the detail is given below in subsection. a folder with the name of dbt project will appear. here the dbt project name is `nyc_parking_violations`.
6. make a `nyc_parking_violations\profiles.yml` file. sample available
7. the first line in `profiles.yml` should be identical to the profile given in `dbt_project.yml` line 9. this ensures the connection of profile with the dbt project. To verify this, open `nyc_parking_violations` folder in terminal and run the command `dbt debug`. If the tests are passed and the connection is OK, than we are good to go.
8. open the `models` folder. Delete everything. Create a new file here `first_model.sql` and write a sql query in this file.

## 5. to create a dbt project
- run the command : ``` dbt init ```
- give the name of the project
- give the backend database number
