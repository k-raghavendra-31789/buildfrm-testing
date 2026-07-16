catalog_name = "traffic_lakehouse"
bronze_schema_name = f"{catalog_name}.bronze"
silver_schema_name = f"{catalog_name}.silver"

results = []

# Create catalog if needed
existing_catalogs = [row.catalog for row in spark.sql("SHOW CATALOGS").collect()]
if catalog_name in existing_catalogs:
    results.append(("catalog", catalog_name, "Already existed"))
else:
    spark.sql(f"CREATE CATALOG IF NOT EXISTS {catalog_name}")
    results.append(("catalog", catalog_name, "Created"))

# Create bronze schema if needed
existing_schemas = [row.databaseName for row in spark.sql(f"SHOW SCHEMAS IN {catalog_name}").collect()]
if "bronze" in existing_schemas:
    results.append(("schema", bronze_schema_name, "Already existed"))
else:
    spark.sql(f"CREATE SCHEMA IF NOT EXISTS {bronze_schema_name}")
    results.append(("schema", bronze_schema_name, "Created"))

# Create silver schema if needed
existing_schemas = [row.databaseName for row in spark.sql(f"SHOW SCHEMAS IN {catalog_name}").collect()]
if "silver" in existing_schemas:
    results.append(("schema", silver_schema_name, "Already existed"))
else:
    spark.sql(f"CREATE SCHEMA IF NOT EXISTS {silver_schema_name}")
    results.append(("schema", silver_schema_name, "Created"))

# Verification
print("Verification:")
for obj_type, name, status in results:
    print(f"{obj_type}: {name} -> {status}")
