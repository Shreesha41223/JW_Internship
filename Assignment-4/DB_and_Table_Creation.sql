CREATE DATABASE db;

CREATE TABLE db.employee (  EmpNo INT PRIMARY KEY,     Ename varchar(20),     Sal int,     Hire_Date varchar(12),     Commission int,     DeptNo int,     Mgr int );
create table db.department (  DeptNo int primary key,     Dname varchar(20),     Loc varchar(20) );

INSERT INTO `db`.`department` (`DeptNo`, `Dname`, `Loc`) VALUES ('10', 'Accounts', 'Bangalore');
INSERT INTO `db`.`department` (`DeptNo`, `Dname`, `Loc`) VALUES ('20', 'IT', 'Delhi');
INSERT INTO `db`.`department` (`DeptNo`, `Dname`, `Loc`) VALUES ('30', 'Production', 'Chennai');
INSERT INTO `db`.`department` (`DeptNo`, `Dname`, `Loc`) VALUES ('40', 'Sales', 'Hyd');
INSERT INTO `db`.`department` (`DeptNo`, `Dname`, `Loc`) VALUES ('50', 'Admin', 'London');

alter table db.employee add foreign key (DeptNo) references db.department (DeptNo);

INSERT INTO `db`.`employee` (`EmpNo`, `Ename`, `Sal`, `Hire_Date`, `Commission`, `DeptNo`, `Mgr`) VALUES ('1001', 'Sachin', '19000', '1-Jan-1980', '2100', '20', '1003');
INSERT INTO `db`.`employee` (`EmpNo`, `Ename`, `Sal`, `Hire_Date`, `Commission`, `DeptNo`, `Mgr`) VALUES ('1002', 'Kapil', '15000', '1-Jan-1970', '2300', '10', '1003');
INSERT INTO `db`.`employee` (`EmpNo`, `Ename`, `Sal`, `Hire_Date`, `Commission`, `DeptNo`, `Mgr`) VALUES ('1003', 'Stefen', '12000', '1-Jan-1990', '500', '20', '1007');
INSERT INTO `db`.`employee` (`EmpNo`, `Ename`, `Sal`, `Hire_Date`, `DeptNo`, `Mgr`) VALUES ('1004', 'Williams', '9000', '1-Jan-2001', '30', '1007');
INSERT INTO `db`.`employee` (`EmpNo`, `Ename`, `Sal`, `Hire_Date`, `DeptNo`, `Mgr`) VALUES ('1005', 'John', '5000', '1-Jan-2005', '30', '1006');
INSERT INTO `db`.`employee` (`EmpNo`, `Ename`, `Sal`, `Hire_Date`, `Commission`, `DeptNo`, `Mgr`) VALUES ('1006', 'Dravid', '19000', '1-Jan-1985', '2400', '10', '1007');
INSERT INTO `db`.`employee` (`EmpNo`, `Ename`, `Sal`, `Hire_Date`, `Commission`) VALUES ('1007', 'Martin', '21000', '1-Jan-2000', '1040');

