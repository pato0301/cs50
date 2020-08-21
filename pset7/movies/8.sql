SELECT distinct p.name
FROM "movies" m
left join stars s on (s.movie_id=m.id)
left join people p on (p.id=s.person_id)
where m.title like "Toy Story"
order by p.name;