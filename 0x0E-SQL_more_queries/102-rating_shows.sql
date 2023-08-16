-- Rotten tomatoes
-- Lists shws by their rating
SELECT t.title, SUM(tv_show_ratings.rate) AS rating
FROM tv_shows AS t INNER JOIN tv_show_ratings AS tr
ON t.id = tr.show_id
GROUP BY t.id ORDER BY rating DESC;
