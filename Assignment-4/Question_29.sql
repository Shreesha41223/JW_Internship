select
	M.*
from
	db.employee E
join 
	db.employee M on E.Mgr = M.EmpNo
join
	db.department D on E.DeptNo = D.DeptNo
where
	M.Commission < 1000 and D.Loc = 'Delhi';