with kevin as (SELECT m.title,m.id, s.person_id, p.name as name,
(case when s.person_id = (select id from people p where p.name = "Kevin Bacon" and p.birth = 1958) then "y"
else "n"
end) as kevin
FROM movies m
left join stars s on (m.id=s.movie_id)
left join people p on (s.person_id=p.id))
select distinct p.name as name
FROM stars s
left join kevin k on (s.movie_id=k.id)
left join movies m on (s.movie_id=m.id)
left join people p on (s.person_id=p.id)
where k.kevin ="y"
and s.person_id not in (select id from people p where p.name = "Kevin Bacon" and p.birth = 1958);