select
	replace(Ename, 'a', '#') as modified_Ename,
    Ename -- for comparision with the actual value
from db.employee;

-- =======================
-- modified_Ename	Ename
-- =======================
-- S#chin			Sachin
-- K#pil			Kapil
-- Stefen			Stefen
-- Willi#ms			Williams
-- John				John
-- Dr#vid			Dravid
-- M#rtin			Martin
-- =======================