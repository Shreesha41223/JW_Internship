delete from db.employee
where DeptNo in ( select DeptNo from db.department where Loc = 'Chennai');

select * from db.employee;


-- =============================================================
-- EmpNo	Ename	Sal		Hire_Date	Commission	DeptNo	Mgr
-- =============================================================
-- 1001		Sachin	20900	1-Jan-1980	2100		20		1003
-- 1002		Kapil	16500	1-Jan-1970	2300		10		1003
-- 1003		Stefen	13200	1-Jan-1990	500			20		1007
-- 1006		Dravid	20900	1-Jan-1985	2400		10		1007
-- 1007		Martin	23100	1-Jan-2000	1040	
-- =============================================================	