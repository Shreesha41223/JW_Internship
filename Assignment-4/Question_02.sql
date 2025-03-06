select D.*
from db.department as D
join (
	select
		DeptNo,
        count(*) as EmpCount
	from db.employee
    group by DeptNo
    having count(*) > 1
) as E on D.DeptNo = E.DeptNo;


-- ==========================
-- DeptNo	Dname	Loc 
-- ==========================
-- 10	Accounts	Bangalore
-- 20	IT	Delhi
-- 30	Production	Chennai
-- ==========================