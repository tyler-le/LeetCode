# Write your MySQL query statement below

-- SELECT unique_id, name
SELECT unique_id, name
FROM Employees e
LEFT JOIN EmployeeUNI euni ON e.id=euni.id