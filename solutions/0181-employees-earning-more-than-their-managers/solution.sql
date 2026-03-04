select e.name as "Employee" from Employee as e where salary>(select salary from employee where e.managerid=id)
