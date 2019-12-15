-- Product Sales Analysis I
select p.product_name, s.year, s.price
from sales s
join product p
on s.product_id = p.product_id

-- Product Sales Analysis II
select product_id, sum(quantity) as total_quantity
from sales
group by product_id

-- Swap Salary
update salary
set sex = case
    when sex = 'm' then 'f'
    else 'm'
end;

-- Exchange Seats
select
    (case
        when mod(id, 2) != 0 and id != counts then id + 1
        when mod(id, 2) != 0 and id = counts then id
        else id - 1
    end) as id,
    student
from seat,
    (select count(*) as counts from seat) as seat_counts
order by id

-- Game Play Analysis I
select player_id, min(event_date) as first_login
from activity
group by player_id

-- Big Countries
select name, population, area
from World
where area > 3000000 or population > 25000000

-- Shortest Distance in a Line
solution1: SELECT MIN(ABS(p2.x - p1.x)) AS shortest FROM point AS p1, point AS p2 WHERE p1.x <> p2.x;
solution2: SELECT MIN(p2.x - p1.x) AS shortest FROM point AS p1, point AS p2 WHERE p1.x < p2.x;


-- Immediate Food Delivery I
select round(100*sum(case when order_date=customer_pref_delivery_date then 1 else 0 end)/count(1), 2) immediate_percentage
from Delivery

-- Immediate Food Delivery II
select round(100*sum(case when order_date=customer_pref_delivery_date then 1 else 0 end)/count(distinct customer_id), 2) immediate_percentage
from Delivery
where (customer_id, order_date) in
    (select customer_id, min(order_date)
    from Delivery
    group by customer_id)

-- Actors and Directors Who Cooperated At Least Three Times
select actor_id, director_id
from ActorDirector
group by actor_id, director_id
having count(*) >= 3

-- Project Employees III
select p.project_id, e.experience_years
from Project p
inner join Employee e on p.employee_id = e.employee_id
where p.project_id, e.experience_years in (
    select p.project_id, max(experience_years) as experience_years
    from Project p
    inner join Employee e on p.employee_id = e.employee_id
    group p.project_id
)

-- Sales Analysis I
select *
from Sales
group by saller_id
having sum(price) = select max(sum(price)) as price from Sales group by saller_id

-- Active Businesses
select a.business_id
from Events as a
join (select event_type, avg(occurences) occurence_avg from Events group by event_type) as b
on a.event_type = b.event_type
where occurences > occurence_avg
group by a.business_id
having count(*) > 1

-- Reformat Department Table
select id,
    sum(IF(month = 'Jan', revenue, NULL)) as Jan_Revenue,
    sum(IF(month = 'Feb', revenue, NULL)) as Feb_Revenue,
    sum(IF(month = 'Mar', revenue, NULL)) as Mar_Revenue,
    sum(IF(month = 'Apr', revenue, NULL)) as Apr_Revenue,
    sum(IF(month = 'May', revenue, NULL)) as May_Revenue,
    sum(IF(month = 'Jun', revenue, NULL)) as Jun_Revenue,
    sum(IF(month = 'Jul', revenue, NULL)) as Jul_Revenue,
    sum(IF(month = 'Aug', revenue, NULL)) as Aug_Revenue,
    sum(IF(month = 'Sep', revenue, NULL)) as Sep_Revenue,
    sum(IF(month = 'Oct', revenue, NULL)) as Oct_Revenue,
    sum(IF(month = 'Nov', revenue, NULL)) as Nov_Revenue,
    sum(IF(month = 'Dec', revenue, NULL)) as Dec_Revenue
from Department
group by id
order by id

-- Combine Two Tables
select FirstName, LastName, City, State
from Person
left join Address
on Person.PersonId = Address.PersonId

-- Employees Earning More Than Their Managers
select a.Name as Employee
from Employee as a
inner join Employee as b
on a.ManagerId = b.Id
where a.Salary > b.Salary

-- Customers Who Never Order
select Customers.Name as Customers
from Customers
left join Orders
on Customers.Id = Orders.CustomerId
where Orders.ID is NULL

-- Rank Scores
select b.score, count(*) as Rank
from
    (select distinct score from Scores) as a, Scores as b
where a.score >= b.score
group by b.id, b.score
order by b.score desc;

-- Classes More Than 5 Students
select class
from courses
group by class
having count(distinct student) >= 5

-- Rising Temperature
select a.Id
from Weather as a
inner join Weather as b
on b.RecordDate = a.RecordDate - INTERVAL 1 DAY
where a.Temperature > b.Temperature

-- Delete Duplicate Emails
DELETE p1 FROM Person p1,
    Person p2
WHERE
    p1.Email = p2.Email AND p1.Id > p2.Id

-- Consecutive Numbers
SELECT DISTINCT
    l1.Num AS ConsecutiveNums
FROM
    Logs l1,
    Logs l2,
    Logs l3
WHERE
    l1.Id = l2.Id - 1
    AND l2.Id = l3.Id - 1
    AND l1.Num = l2.Num
    AND l2.Num = l3.Num
;

-- Second Highest Salary
SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT 1 OFFSET 1

-- Nth Highest Salary
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE M INT;
SET M=N-1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT 1 OFFSET M
  );
END