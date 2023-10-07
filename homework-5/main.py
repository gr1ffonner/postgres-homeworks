import json

import psycopg2
from psycopg2 import sql
from config import config


def main():
    script_file = 'fill_db.sql'
    json_file = 'suppliers.json'
    db_name = 'homework_5'

    params = config()
    conn = None

    # create_database(params, db_name)
    print(f"БД {db_name} успешно создана")

    params.update({'dbname': db_name})
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                # execute_sql_script(cur, script_file)
                print(f"БД {db_name} успешно заполнена")

                # create_suppliers_table(cur)
                print("Таблица suppliers успешно создана")

                # suppliers = get_suppliers_data(json_file)
                # insert_suppliers_data(cur, suppliers)
                print("Данные в suppliers успешно добавлены")

                add_foreign_keys(cur)
                print(f"FOREIGN KEY успешно добавлены")

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()



def create_database(params, db_name) -> None:
    """Создает новую базу данных."""
    conn = psycopg2.connect(**params)
    conn.autocommit = True
    with conn.cursor() as cur:
        cur.execute(sql.SQL("CREATE DATABASE {}").format(
            sql.Identifier(db_name))
        )
    conn.close()


def execute_sql_script(cur, script_file) -> None:
    """Выполняет скрипт из файла для заполнения БД данными."""
    cur.execute(open("fill_db.sql", "r").read())


def create_suppliers_table(cur) -> None:
    """Создает таблицу suppliers."""
    cur.execute("""CREATE TABLE suppliers (
    supplier_id integer PRIMARY KEY,
    company_name varchar,
    contact varchar, 
    address varchar,
    phone varchar,
    fax varchar, 
    homepage varchar, 
    products varchar[]
    );""")


def get_suppliers_data(json_file: str) -> list[dict]:
    """Извлекает данные о поставщиках из JSON-файла и возвращает список словарей с соответствующей информацией."""
    with open(json_file) as file:
        data = json.load(file)
    return data


def insert_suppliers_data(cur, suppliers: list[dict]) -> None:
    """Добавляет данные из suppliers.json в таблицу suppliers."""
    try:
        for i, row in enumerate(suppliers):
            company_name = row["company_name"]
            contact = row["contact"]
            address = row["address"]
            phone = row["phone"]
            fax = row["fax"]
            homepage = row["homepage"]
            products = row["products"]
            cur.execute(
                "INSERT INTO suppliers (supplier_id, company_name, contact, address, phone, fax, homepage, products)"
                " VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                [i, company_name, contact, address, phone, fax, homepage, products]
            )
    except psycopg2.Error as e:
        print(f"Error inserting data: {e}")



def add_foreign_keys(cur) -> None:
    """Добавляет foreign key со ссылкой на supplier_id в таблицу products."""
    cur.execute(
        """
        ALTER TABLE products
        ADD COLUMN supplier_id integer;
        ALTER TABLE products
        ADD CONSTRAINT fk_supplier_id
        FOREIGN KEY (supplier_id)
        REFERENCES suppliers (supplier_id); 
        """
    )


if __name__ == '__main__':
    main()
