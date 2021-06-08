--1
-- products.name by cust customers.name

SELECT customers.name, products.name
FROM customers
INNER JOIN products ON customers.id=products.id
;

--2
-- Product name from cust

SELECT customer.email, customer.phone_number, products.name
FROM customers
INNER JOIN products ON customers.id=products.id
;

--3
-- company of product  

SELECT products_id, products.name, company.name
FROM product
INNER JOIN company ON products.id=company.id
;

--4
-- basket cost and product id by customers   

SELECT customers.name, basket.cost, basket.products_id, products.id 
FROM customers
INNER JOIN basket ON customers.id=basket.id
INNER JOIN product ON basket.products_id=products.id
;


--5
-- company from cost of product    

SELECT products_id, product.name, products.cost, company.id
FROM product
INNER JOIN company ON product.id=company.id
INNER JOIN company ON product.cost=company.id
;

--6
-- customer by basket id and cost  

SELECT customers.name, basket.id
FROM basket
INNER JOIN customers ON basket.id=customers.id
INNER JOIN customers ON basket.cost=customers.id
;

--7
-- location of customers by basket cost  

SELECT customers.name, basket.cost, customers.location
FROM basket
INNER JOIN customers ON basket.id=customers.id
;

--8
-- company by product id

SELECT products.id, company.id
FROM products
INNER JOIN company ON product.id=company.products_id
;

--9
-- customers name from las name and email

SELECT customers.email, customers.name
FROM customers
INNER JOIN basket ON customers.id=basket.id
;

--10
-- customers from products name and company

SELECT products.name, company.id, customers.name
FROM company
INNER JOIN customers ON company.products_id=customers.id
INNER JOIN customers ON products.name=customers.id
;


