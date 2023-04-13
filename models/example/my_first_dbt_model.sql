{{ config(materialized='table') }}

WITH source_data AS (

  SELECT 1 AS id
        , 'B' AS trade_code
  UNION ALL
  SELECT null AS id
        , 'S' AS trade_code

)

SELECT *
FROM source_data
