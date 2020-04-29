-- Write a SQL query to get the nth highest salary from the Employee table.

-- +----+--------+
-- | Id | Salary |
-- +----+--------+
-- | 1  | 100    |
-- | 2  | 200    |
-- | 3  | 300    |
-- +----+--------+

-- For example, given the above Employee table, the nth highest salary where n = 2 is 200. 
-- If there is no nth highest salary, then the query should return null.

-- +------------------------+
-- | getNthHighestSalary(2) |
-- +------------------------+
-- | 200                    |
-- +------------------------+

-- LIMIT 子句可以被用于强制 SELECT 语句返回指定的记录数。LIMIT 接受一个或两个数字参数。参数必须是一个整数常量。
-- 如果给定两个参数，第一个参数指定第一个返回记录行的偏移量，第二个参数指定返回记录行的最大数目

-- 创建function 语法
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    DECLARE temp integer;
    SET temp = N - 1;
    RETURN(
        SELECT IFNULL((SELECT DISTINCT Salary from Employee order by Salary DESC LIMIT temp, 1), null)
    )
END