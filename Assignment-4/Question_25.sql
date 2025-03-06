select
	M.Ename
from
	db.employee E
join
	db.employee M on E.Mgr = M.EmpNo
group by
	E.Mgr
order by
	count(*) desc
limit 1;