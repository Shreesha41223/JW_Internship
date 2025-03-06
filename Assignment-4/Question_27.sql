select
	M.*
from 
	db.employee M
join
	db.employee E on E.Mgr = M.EmpNo
group by
	M.EmpNo
    
-- =============================================================
-- EmpNo	Ename	Sal		Hire_Date	Commission	DeptNo	Mgr
-- =============================================================
-- 1003		Stefen	13200	1-Jan-1990	500			20		1007
-- 1007		Martin	23100	1-Jan-2000	1040		
-- =============================================================