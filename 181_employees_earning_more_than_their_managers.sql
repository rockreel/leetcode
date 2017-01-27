# Write your MySQL query statement below
SELECT E.Name AS Employee
FROM Employee AS E
LEFT JOIN Employee AS M
ON E.ManagerId = M.ID
WHERE E.Salary > M.Salary;

