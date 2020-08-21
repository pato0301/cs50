with personas as (select distinct s.person_id as person_id
from stars s
left join movies m on s.movie_id = m.id
WHERE m.year = 2004)
SELECT p.name as name
from people p
left join personas ps on (p.id=ps.person_id)
where ps.person_id is not null
order by p.birth asc;