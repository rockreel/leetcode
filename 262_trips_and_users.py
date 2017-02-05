# Write your MySQL query statement below
SELECT 
  Request_at AS Day,
  ROUND(SUM(IF(Status!='completed', 1, 0))/SUM(1), 2) AS `Cancellation Rate`
FROM Trips
JOIN Users
ON Trips.Client_Id = Users.Users_Id
WHERE Users.Banned = 'No'
AND Request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY Request_at;

