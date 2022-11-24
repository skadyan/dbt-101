{{ config(materialized='table') }}

WITH source_data AS (

  SELECT 1 AS id
  UNION ALL
  SELECT null AS id

)

SELECT *
FROM source_data
