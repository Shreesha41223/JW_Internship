SELECT 
    M.*, 
    DATE('now') - M.Hire_Date AS TotalExperience  
FROM 
    db.employee E
JOIN 
    db.employee M ON E.Mgr = M.EmpNo
group by 
	E.Mgr;