select
	E.*,
    D.*,
    M.*
from
	db.employee E
join
	db.department D on E.DeptNo = D.DeptNo
left join
	db.employee M on E.Mgr = M.EmpNo
where
	E.Sal = (
		select distinct Sal 
		from db.employee 
        order by Sal desc 
        limit 1 offset 1);
        
        
-- ============================================================================================================================================================
-- EmpNo	Ename	Sal		Hire_Date	Commission	DeptNo	Mgr		DeptNo	Dname		Loc			EmpNo	Ename	Sal		Hire_Date	Commission	DeptNo	Mgr
-- ============================================================================================================================================================
-- 1001		Sachin	20900	1-Jan-1980	2100		20		1003	20		IT			Delhi		1003	Stefen	13200	1-Jan-1990	500			20	1007
-- 1006		Dravid	20900	1-Jan-1985	2400		10		1007	10		Accounts	Bangalore	1007	Martin	23100	1-Jan-2000	1040		
-- ============================================================================================================================================================