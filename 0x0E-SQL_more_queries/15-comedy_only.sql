-- Only comedy
-- lists all comedy shows
SELECT t.title
FROM t JOIN tv_show_genres AS tg
ON tg.show_id = t.id JOIN tv_genres
ON tg.genre_id = tv_genres.id
WHERE tv_genres.name = "Comedy"
ORDER BY t.title;
