-- Only comedy
-- lists all comedy shows
SELECT t.title FROM tv_shows AS t
JOIN tv_show_genres AS tg ON t.id = tg.show_id
JOIN tv_genres ON tg.genre_id = tv_genres.id
WHERE name = "Comedy"
ORDER BY t.title ASC;
