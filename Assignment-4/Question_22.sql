select 
    E.*
from 
    db.employee E
join 
    db.department D on E.DeptNo = D.DeptNo
where 
    D.Loc = 'Bangalore';