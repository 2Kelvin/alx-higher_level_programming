--Say my name
-- Lists all second_table records
SELECT score, name FROM second_table
  WHERE name != "" AND IS NOT NULL
    ORDER BY score DESC;
