-- Only comedy
-- lists all comedy shows
SELECT tv_shows.title FROM tv_shows
INNER JOIN tv_show_genres AS tg ON tg.show_id = t.id
INNER JOIN tv_genres ON tg.genre_id = tv_genres.id
WHERE tv_genres.name = "Comedy"
ORDER BY tv_shows.title;
