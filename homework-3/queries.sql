-- Напишите запросы, которые выводят следующую информацию:
-- 1. Название компании заказчика (company_name из табл. customers) и ФИО сотрудника, работающего над заказом этой компании (см таблицу employees),
-- когда и заказчик и сотрудник зарегистрированы в городе London, а доставку заказа ведет компания United Package (company_name в табл shippers)
SELECT C.company_name, CONCAT(E.first_name, ' ', E.last_name) AS employee
FROM Orders O
JOIN Employees E ON O.employee_id = E.employee_id
JOIN customers C ON O.customer_id = C.customer_id
JOIN shippers S ON O.ship_via = S.shipper_id
WHERE E.city = 'London' AND C.city = 'London' AND S.shipper_id = 2;

-- 2. Наименование продукта, количество товара (product_name и units_in_stock в табл products),
-- имя поставщика и его телефон (contact_name и phone в табл suppliers) для таких продуктов,
-- которые не сняты с продажи (поле discontinued) и которых меньше 25 и которые в категориях Dairy Products и Condiments.
-- Отсортировать результат по возрастанию количества оставшегося товара.
SELECT S.contact_name, S.phone, P.product_name, P.units_in_stock
FROM products P
JOIN suppliers S ON P.supplier_id = S.supplier_id
JOIN categories C ON P.category_id = C.category_id
WHERE P.discontinued != 1 AND P.units_in_stock < 25
AND C.category_name IN ('Dairy Products', 'Condiments')
ORDER BY P.units_in_stock;

-- 3. Список компаний заказчиков (company_name из табл customers), не сделавших ни одного заказа
SELECT C.company_name
FROM customers AS C
LEFT JOIN orders O ON C.customer_id = O.customer_id
WHERE O.order_id IS NULL;

-- 4. уникальные названия продуктов, которых заказано ровно 10 единиц (количество заказанных единиц см в колонке quantity табл order_details)
-- Этот запрос написать именно с использованием подзапроса.
SELECT DISTINCT product_name
FROM products
WHERE product_id IN (
    SELECT product_id
    FROM order_details
    WHERE quantity = 10
);
