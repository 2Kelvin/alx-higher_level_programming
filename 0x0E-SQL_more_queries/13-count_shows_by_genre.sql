-- Number of shows by genre
-- Lists no of shows linked to each genre
SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows
FROM tv_show_genres AS tg LEFT JOIN tv_genres
ON tg.genre_id=tv_genres.id GROUP BY genre
ORDER BY number_of_shows DESC;
