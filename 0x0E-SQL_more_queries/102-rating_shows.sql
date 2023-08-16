-- Rotten tomatoes
-- Lists shws by their rating
SELECT title, SUM(tv_show_ratings.rate) AS rating
FROM tv_shows AS t LEFT JOIN tv_show_ratings AS tr
ON t.id = tr.show_id
GROUP BY title
ORDER BY rating DESC;
