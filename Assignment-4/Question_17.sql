select
	D.Loc,
	count(E.EmpNo) as EmployeeCount
from 
	db.department D
left join
	db.employee E on D.DeptNo = E.DeptNo
group by D.Loc;

-- ==================================
-- Loc			EmployeeCount
-- ==================================
-- Bangalore	2
-- Delhi		2
-- Chennai		0
-- Hyd			0
-- London		0