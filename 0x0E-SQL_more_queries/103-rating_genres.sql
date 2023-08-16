-- Best Genre
-- Lists all genres by their rating
SELECT name, SUM(tv_show_ratings.rate) AS rating
FROM tv_genres as tg INNER JOIN tv_show_genres AS tsg
ON tg.id = tsg.genre_id INNER JOIN tv_show_ratings AS tr
ON tsg.show_id = tr.show_id
GROUP BY name
ORDER BY rating DESC;
