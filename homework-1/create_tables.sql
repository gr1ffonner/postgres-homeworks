-- SQL-команды для создания таблиц
create table Orders (
	order_id integer primary key,
	order_date date,
	ship_city varchar (25),
	customer_id varchar (5) references Customers(customer_id),
	employee_id integer references Employees(employee_id)
);

create table Customers (
  customer_id varchar (5) primary key,
  company_name varchar (50),
  contact_name varchar (50)
);

create table Employees (
  employee_id integer primary key,
  first_name varchar (50),
  last_name varchar (50),
  title varchar (100),
  birth_date date,
  notes text
);