-- My genres
-- Lists all gbres of the show Dexter
SELECT tv_genres.name
FROM tv_show_genres AS tg JOIN tv_shows AS t
ON tg.show_id = t.id JOIN tv_genres
ON tg.genre_id = tv_genres.id
WHERE t.title = "Dexter"
ORDER BY tv_genres.name;
