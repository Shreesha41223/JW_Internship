select
	Ename,
    Sal + coalesce(Commission, 0) as Gross_Salary
from db.employee;

-- ======================
-- Ename	Gross_Salary
-- ======================
-- Sachin	23000
-- Kapil	18800
-- Stefen	13700
-- Dravid	23300
-- Martin	24140
-- ======================