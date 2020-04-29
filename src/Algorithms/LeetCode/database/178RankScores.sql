-- Write a SQL query to rank scores. If there is a tie between two scores, both should have the same ranking. Note that after a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no "holes" between ranks.

-- +----+-------+
-- | Id | Score |
-- +----+-------+
-- | 1  | 3.50  |
-- | 2  | 3.65  |
-- | 3  | 4.00  |
-- | 4  | 3.85  |
-- | 5  | 4.00  |
-- | 6  | 3.65  |
-- +----+-------+

-- For example, given the above Scores table, your query should generate the following report (order by highest score):

-- +-------+------+
-- | Score | Rank |
-- +-------+------+
-- | 4.00  | 1    |
-- | 4.00  | 1    |
-- | 3.85  | 2    |
-- | 3.65  | 3    |
-- | 3.65  | 3    |
-- | 3.50  | 4    |
-- +-------+------+

-- https://www.bbsmax.com/A/ke5jkjgdrl/

-- method 1
select Score as score,
(select count(*) from 
(select DISTINCT Score as s from Scores) as t
where s >= Score) as Rank
from Scores
order by Score DESC;

-- method 2
select s.Score as score, COUNT(DISTINCT t.Score) as Rank
from Scores as s
join Scores as t 
on s.Score <= t.Score 
group by s.Id
order by s.Score DESC
