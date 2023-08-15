-- Sort score >= 10
-- Lists records with a score of above 10
SELECT score, name FROM second_table
  WHERE score>=10
    ORDER BY score DESC;
