select
	E.*
from 
	db.employee E
join
	db.employee M on E.Mgr = M.EmpNo
where
	M.Ename = 'Stefen';
    
-- =============================================================
-- EmpNo	Ename	Sal		Hire_Date	Commission	DeptNo	Mgr
-- =============================================================
-- 1001		Sachin	20900	1-Jan-1980	2100		20		1003
-- 1002		Kapil	16500	1-Jan-1970	2300		10		1003
-- =============================================================