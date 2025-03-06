update db.employee
set Sal = Sal * 1.10
where EmpNo > 0;

select Sal as UpdatedSalary from db.employee;

-- =============
-- UpdatedSalary
-- =============
-- 20900
-- 16500
-- 13200
-- 9900
-- 5500
-- 20900
-- 23100
-- =============