-- No comedy tonight
-- list non-comedy genre shows
SELECT t.title FROM tv_shows AS t
WHERE t.id NOT IN (
    SELECT t.id FROM t
    INNER JOIN tv_show_genres AS tsg
    ON t.id = tsg.show_id INNER JOIN tv_genres AS tg
    ON tsg.genre_id = tg.id
    WHERE tg.name = "Comedy")
ORDER BY t.title;
