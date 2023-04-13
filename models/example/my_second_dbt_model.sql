SELECT
  m.*,
  r.*
FROM {{ ref('my_first_dbt_model') }} AS m,
 {{ ref('trade_types') }} AS r
WHERE m.id = 1
AND m.trade_code = r.type_code
