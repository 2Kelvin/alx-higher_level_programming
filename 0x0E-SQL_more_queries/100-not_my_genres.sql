-- Not my genre
-- lists NOT Dexter genres
SELECT tv_genres.name FROM tv_genres AS tvg
WHERE tvg.id NOT IN (
    SELECT tvg.id FROM tvg
    INNER JOIN tv_show_genres AS tsg
    ON tvg.id = tsg.genre_id INNER JOIN tv_shows AS t
    ON tsg.show_id = t.id WHERE t.title = "Dexter")
ORDER BY tvg.name;
