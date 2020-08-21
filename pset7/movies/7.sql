SELECT m.title ,r.rating
FROM "movies" m
left join ratings r on (r.movie_id=m.id)
where m.year = 2010 and r.rating is not null
order by r.rating desc, m.title asc;