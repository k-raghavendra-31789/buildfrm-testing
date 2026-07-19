# Databricks notebook source
# COMMAND ----------
catalog = 'traffic_lakehouse'
bronze_schema = 'bronze'
silver_schema = 'silver'

print('Validating Unity Catalog setup for BLDFM01-6')

catalog_status = 'Already existed'
bronze_status = 'Already existed'
silver_status = 'Already existed'

existing_catalogs = [row.catalog for row in spark.sql('SHOW CATALOGS').collect()]
if catalog not in existing_catalogs:
    spark.sql(f'CREATE CATALOG IF NOT EXISTS {catalog}')
    catalog_status = 'Created'

existing_schemas = [row.databaseName for row in spark.sql(f'SHOW SCHEMAS IN {catalog}').collect()]
if bronze_schema not in existing_schemas:
    spark.sql(f'CREATE SCHEMA IF NOT EXISTS {catalog}.{bronze_schema}')
    bronze_status = 'Created'

existing_schemas = [row.databaseName for row in spark.sql(f'SHOW SCHEMAS IN {catalog}').collect()]
if silver_schema not in existing_schemas:
    spark.sql(f'CREATE SCHEMA IF NOT EXISTS {catalog}.{silver_schema}')
    silver_status = 'Created'

print(f'Catalog {catalog}: {catalog_status}')
print(f'Schema {catalog}.{bronze_schema}: {bronze_status}')
print(f'Schema {catalog}.{silver_schema}: {silver_status}')

print('\nSHOW CATALOGS:')
display(spark.sql('SHOW CATALOGS'))

print(f'\nSHOW SCHEMAS IN {catalog}:')
display(spark.sql(f'SHOW SCHEMAS IN {catalog}'))
