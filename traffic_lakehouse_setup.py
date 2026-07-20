# Databricks notebook source
# COMMAND ----------
from pyspark.sql import functions as F

catalog = "traffic_lakehouse"
bronze_schema = "bronze"
silver_schema = "silver"

existing_catalogs = {row[0] for row in spark.sql("SHOW CATALOGS").collect()}
created_catalog = catalog not in existing_catalogs

spark.sql(f"CREATE CATALOG IF NOT EXISTS `{catalog}`")
spark.sql(f"CREATE SCHEMA IF NOT EXISTS `{catalog}`.`{bronze_schema}`")
spark.sql(f"CREATE SCHEMA IF NOT EXISTS `{catalog}`.`{silver_schema}`")

print(f"Catalog {catalog}: {'Created' if created_catalog else 'Already existed'}")
print(f"Schema {catalog}.{bronze_schema}: Created or already existed")
print(f"Schema {catalog}.{silver_schema}: Created or already existed")

print('Catalogs check:')
display(spark.sql("SHOW CATALOGS"))
print('Bronze schemas check:')
display(spark.sql(f"SHOW SCHEMAS IN `{catalog}` LIKE '{bronze_schema}'"))
print('Silver schemas check:')
display(spark.sql(f"SHOW SCHEMAS IN `{catalog}` LIKE '{silver_schema}'"))
