select
	E.*
from 
	db.employee E
join
	db.department D on E.DeptNo = D.DeptNo
where 
	D.Loc = 'Bangalore';
    
    
-- =============================================================
-- EmpNo	Ename	Sal		Hire_Date	Commission	DeptNo	Mgr
-- =============================================================
-- 1002		Kapil	16500	1-Jan-1970	2300		10		1003
-- 1006		Dravid	20900	1-Jan-1985	2400		10		1007
-- =============================================================