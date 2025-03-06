select
	E.Ename as EmployeeName,
    M.Ename as ManagerName
from db.employee E
left join
	db.employee M on E.Mgr = M.EmpNo;
    
-- ========================
-- EmployeeName	ManagerName
-- ========================
-- Sachin		Stefen
-- Kapil		Stefen
-- Stefen		Martin
-- Williams		Martin
-- John			Dravid
-- Dravid		Martin
-- Martin
-- ========================