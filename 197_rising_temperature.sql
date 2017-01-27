# Write your MySQL query statement below
SELECT W1.Id AS Id
FROM Weather AS W1
JOIN Weather AS W2
WHERE DATE_SUB(W1.Date, INTERVAL 1 DAY) = W2.Date
AND W1.Temperature > W2.Temperature;

