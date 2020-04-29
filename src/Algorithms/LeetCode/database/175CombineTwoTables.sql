-- Table: Person

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | PersonId    | int     |
-- | FirstName   | varchar |
-- | LastName    | varchar |
-- +-------------+---------+
-- PersonId is the primary key column for this table.

-- Table: Address

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | AddressId   | int     |
-- | PersonId    | int     |
-- | City        | varchar |
-- | State       | varchar |
-- +-------------+---------+
-- AddressId is the primary key column for this table.

-- Write a SQL query for a report that provides the following information for each person in the Person table, 
-- regardless if there is an address for each of those people:
-- FirstName, LastName, City, State

SELECT FirstName, LastName, City, State
FROM Person 
LEFT JOIN Address
ON Person.PersonId = Address.PersonId

-- explain
-- left join(左联接) 返回包括左表中的所有记录和右表中联结字段相等的记录
-- right join(右联接) 返回包括右表中的所有记录和左表中联结字段相等的记录
-- inner join(等值连接) 只返回两个表中联结字段相等的行

