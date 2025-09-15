-- Note to self: used ChatGPT to generate this based on my strategy. 
-- Clearly I'm not quite fluent enough with PostGresql...

WITH parts AS (
  SELECT
    ip,
    split_part(ip, '.', 1) AS a,
    split_part(ip, '.', 2) AS b,
    split_part(ip, '.', 3) AS c,
    split_part(ip, '.', 4) AS d,
    array_length(string_to_array(ip, '.'), 1) AS octet_count
  FROM logs
),
invalid AS (
  SELECT ip
  FROM parts
  WHERE
    -- not exactly 4 octets
    octet_count <> 4
    -- any octet non-numeric
    OR ip !~ '^[0-9]+(\.[0-9]+){3}$'
    -- any octet > 255
    OR (a ~ '^[0-9]+$' AND a::int > 255)
    OR (b ~ '^[0-9]+$' AND b::int > 255)
    OR (c ~ '^[0-9]+$' AND c::int > 255)
    OR (d ~ '^[0-9]+$' AND d::int > 255)
    -- any octet has leading zeros
    OR (length(a) > 1 AND left(a,1) = '0')
    OR (length(b) > 1 AND left(b,1) = '0')
    OR (length(c) > 1 AND left(c,1) = '0')
    OR (length(d) > 1 AND left(d,1) = '0')
)
SELECT ip, COUNT(*) AS invalid_count
FROM invalid
GROUP BY ip
ORDER BY invalid_count DESC, ip DESC;

