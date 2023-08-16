-- Genre ID for all shows
-- Lists all shows in DB: hbtn_0d_tvshows
SELECT t.title, tg.genre_id
FROM tv_shows AS t LEFT JOIN tv_show_genres AS tg
ON tg.show_id = t.id
ORDER BY t.title ASC, tg.genre_id ASC;
