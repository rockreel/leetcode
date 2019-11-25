# Write your MySQL query statement below
SELECT Email
FROM (
  SELECT Email, COUNT(Id) AS Count
  FROM Person
  GROUP BY Email) AS E
WHERE Count > 1;
