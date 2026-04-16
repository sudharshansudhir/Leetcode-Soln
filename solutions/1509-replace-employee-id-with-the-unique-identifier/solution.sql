# Write your MySQL query statement below
select  e.unique_id,em.name from employeeUNI as e right join employees as em on em.id=e.id
