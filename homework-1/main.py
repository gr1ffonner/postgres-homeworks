"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv


north_conn = psycopg2.connect("dbname='north' user='postgres' host='localhost' password='admin'")

print(f"Autocommit: {north_conn.autocommit} and Isolation Level: {north_conn.isolation_level}")

# change the behavior of commit
north_conn.autocommit = True

print(f"Autocommit: {north_conn.autocommit} and Isolation Level: {north_conn.isolation_level}")


def fill_customers_table():
    with north_conn.cursor() as dbtest_curs:
        with open('north_data/customers_data.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cust_id = row['customer_id']
                comp_name = row['company_name']
                contact_name = row['contact_name']
                try:
                    dbtest_curs.execute(f"INSERT INTO customers  VALUES (%s, %s, %s)", [cust_id, comp_name, contact_name])

                except (Exception, psycopg2.DatabaseError) as error:
                    print(error)
# fill_customers_table()


def fill_employees_table():
    with north_conn.cursor() as dbtest_curs:
        with open('north_data/employees_data.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            # "employee_id", "first_name", "last_name", "title", "birth_date", "notes"
            for row in reader:
                empl_id = int(row['employee_id'])
                first_name = row['first_name']
                last_name = row['last_name']
                title = row['title']
                birth_date = row['birth_date']
                notes = row['notes']
                # print(type(notes))
                try:
                    dbtest_curs.execute(f"INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", [empl_id, first_name,
                                                                                                                     last_name, title, birth_date, notes])


                except (Exception, psycopg2.DatabaseError) as error:
                    print(error)
# fill_employees_table()

def fill_orders_table():
    with north_conn.cursor() as dbtest_curs:
        with open('north_data/orders_data.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # "order_id", "customer_id", "employee_id", "order_date", "ship_city"
                order_id = row["order_id"]
                customer_id = row["customer_id"]
                employee_id = row["employee_id"]
                order_date = row["order_date"]
                ship_city = row["ship_city"]
                try:
                    dbtest_curs.execute(f"INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", [order_id, order_date, ship_city, customer_id, employee_id])

                except (Exception, psycopg2.DatabaseError) as error:
                    print(error)

fill_orders_table()