select *
from db.employee
where Hire_Date < date_sub(current_date(), interval 2 year);

-- =========================================================
-- EmpNo Ename 	Sal 	Hire_Date	Commission	DeptNo	Mgr
-- =========================================================
-- 1001	Sachin	19000	1-Jan-1980	2100		20		1003
-- 1002	Kapil	15000	1-Jan-1970	2300		10		1003
-- 1003	Stefen	12000	1-Jan-1990	500			20		1007
-- 1004	Williams 9000	1-Jan-2001				30		1007
-- 1005	John	5000	1-Jan-2005				30		1006
-- 1006	Dravid	19000	1-Jan-1985	2400		10		1007
-- 1007	Martin	21000	1-Jan-2000	1040
-- =========================================================