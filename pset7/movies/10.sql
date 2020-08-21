SELECT distinct p.name
FROM directors d
left join movies m on (d.movie_id=m.id)
left join people p on (d.person_id=p.id)
left join ratings r on (m.id=r.movie_id)
where r.rating >= 9.0;