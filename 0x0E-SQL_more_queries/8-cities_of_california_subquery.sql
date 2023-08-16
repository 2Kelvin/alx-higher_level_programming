-- Cities of California
-- Lists calif cities not found in DB hbtn_0d_usa
SELECT id, name FROM cities
WHERE state_id = (
    SELECT id FROM states
    WHERE name="California")
ORDER BY cities.id ASC;
