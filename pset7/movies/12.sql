with john as (SELECT m.title,m.id,
(case when s.person_id = (select id from people p where p.name = "Johnny Depp") then "y"
else "n"
end) as john
FROM movies m
left join stars s on (m.id=s.movie_id)),
helena as (
SELECT m.title,m.id,
(case when s.person_id = (select id from people p where p.name = "Helena Bonham Carter") then "y"
else "n" end) as helena
FROM movies m
left join stars s on (m.id=s.movie_id))
select distinct m.title
FROM stars s
left join john j on (s.movie_id=j.id)
left join helena h on (s.movie_id=h.id)
left join movies m on (s.movie_id=m.id)
where h.helena = "y" and j.john = "y";