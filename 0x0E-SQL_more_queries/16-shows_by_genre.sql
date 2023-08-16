-- List shows and genres
-- lists all shows & all genres linked to that show
SELECT t.title, tv_genres.name
FROM tv_shows AS t LEFT JOIN tv_show_genres AS tg
ON t.id = tg.show_id LEFT JOIN tv_genres
ON tv_genres.id = tg.genre_id
ORDER BY t.title, tv_genres.name;
