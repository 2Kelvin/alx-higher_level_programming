-- No comedy tonight
-- list non-comedy genre shows
SELECT title FROM tv_shows AS t
WHERE title NOT IN (SELECT title FROM t
    LEFT JOIN tv_show_genres AS tsg
    ON t.id = tsg.show_id LEFT JOIN tv_genres AS tg
    ON tsg.genre_id = tg.id
    WHERE tg.name = "Comedy")
GROUP BY title
ORDER BY title ASC;
