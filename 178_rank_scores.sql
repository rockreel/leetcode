# Write your MySQL query statement below
SELECT Scores.Score AS Score, COUNT(Ranking.Score) AS Rank
  FROM Scores
  JOIN (
       SELECT DISTINCT Score
         FROM Scores
       ) AS Ranking
 WHERE Scores.Score <= Ranking.Score
 GROUP BY Scores.Id, Scores.Score
 ORDER BY Scores.Score DESC;

