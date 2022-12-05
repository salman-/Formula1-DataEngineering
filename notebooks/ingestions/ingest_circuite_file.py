# Databricks notebook source
dbutils.notebook.run("./../helpers/configuration", 0)
dbutils.notebook.run("./../helpers/functions", 0)

circuits_df = read_csv_file(f"{raw_folder_path}/circuits.csv")
circuits_df = make_all_columns_snake_case(circuits_df)
circuits_df = add_time_stamp_to_dataframe(circuits_df, "circuits")

circuits_df = (
    circuits_df.withColumnRenamed("name", "circuit_name")
    .withColumnRenamed("lat", "latitude")
    .withColumnRenamed("lng", "longitude")
    .withColumnRenamed("alt", "altitude")
    .drop("url")
)

save_dataframe_as_parquet(circuits_df, "circiutes")
dbutils.notebook.exit(MESSAGE_TO_WHEN_COMPLETING_NOTEBOOK_SUCCESSFULLY)