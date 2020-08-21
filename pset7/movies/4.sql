SELECT count(rating) as num_max_rate
FROM "movies" m
left join ratings r on (r.movie_id=m.id)
where r.rating = 10.0;