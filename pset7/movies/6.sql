SELECT avg(rating) as avg_rating
FROM "movies" m
left join ratings r on (r.movie_id=m.id)
where m.year = 2012;