CREATE OR REPLACE TABLE myweatherdataproject.weather_dataset.weather_data_table_partitioned_clustered
PARTITION BY DATETIME_TRUNC(dt, YEAR)
CLUSTER BY country
AS SELECT * FROM myweatherdataproject.weather_dataset.weather_data_table;

CREATE OR REPLACE TABLE myweatherdataproject.weather_dataset.weather_data_table_report AS
  SELECT
    country,
    EXTRACT(YEAR from dt) AS year,
    EXTRACT(MONTH from dt) AS month,
    average_temperature,
    average_temperature_uncertainty
  FROM myweatherdataproject.weather_dataset.weather_data_table_partitioned_clustered
  WHERE EXTRACT(YEAR from dt) >= 1990 AND EXTRACT(YEAR from dt) <= 2024
  ORDER BY country ASC, year, month;