-- Temperatures #1
-- Top 3 cities temps descending order; July - August
SELECT CITY, AVG(value) AS avg_temp
  FROM temperatures WHERE month=7 OR month=8
    GROUP BY city
      ORDER BY avg_temp DESC LIMIT 3;
