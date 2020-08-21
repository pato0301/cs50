SELECT m.title
FROM stars s
left join movies m on (s.movie_id=m.id)
left join people p on (s.person_id=p.id)
left join ratings r on (m.id=r.movie_id)
where p.name = "Chadwick Boseman"
order by r.rating desc
limit 5;