select
	D.Dname,
    sum(E.Sal) as Salary
from db.department D
left join
	db.employee E on D.DeptNo = E.DeptNo
group by Dname;

-- ===================
-- Dname		Salary
-- ===================
-- Accounts		34000
-- IT			31000
-- Production	14000
-- Sales	
-- Admin	
-- ===================