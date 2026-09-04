-- Write your query below
select c.name from customers c
LEFT join orders o 
    on c.id = o.customer_id
where o.id is Null 