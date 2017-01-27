# Write your MySQL query statement below
SELECT
  Department.Name AS Department,
  Employee.Name AS Employee,
  Employee.Salary AS Salary
FROM (
  SELECT MAX(Salary) AS Salary, DepartmentId
  FROM Employee
  GROUP BY DepartmentId) AS M
LEFT JOIN Employee
ON Employee.Salary = M.Salary AND Employee.DepartmentId = M.DepartmentId
JOIN Department
ON Department.Id = Employee.DepartmentId;

