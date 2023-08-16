-- Not my genre
-- lists NOT Dexter genres
SELECT name FROM tv_genres AS tvg
WHERE name NOT IN (SELECT name FROM tvg
    LEFT JOIN tv_show_genres AS tsg
    ON tvg.id = tsg.genre_id LEFT JOIN tv_shows AS t
    ON tsg.show_id = t.id
    WHERE t.title = "Dexter")
GROUP BY name
ORDER BY name ASC;
