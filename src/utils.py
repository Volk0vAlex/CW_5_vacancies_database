import psycopg2


def create_database(database_name: str, params: dict) -> None:
    """Создание базы данных и таблиц для сохранения данных о каналах и видео."""
    print("Создаем и заполняем базу...\n")

    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f"DROP DATABASE IF EXISTS {database_name}")
    cur.execute(f"CREATE DATABASE {database_name}")
    conn.commit()

    cur.close()
    conn.close()

    conn = psycopg2.connect(dbname=database_name, **params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(open("queries.sql", "r", encoding="utf-8").read())
    conn.commit()

    cur.close()
    conn.close()


def insert_employers(employers_list, database_name: str, params: dict):
    """Вставляем работодателей"""
    conn = psycopg2.connect(dbname=database_name, **params)
    conn.autocommit = True
    cur = conn.cursor()

    postgres_insert_query = """ INSERT INTO employers (id, name, city)
                                           VALUES (%s,%s,%s)"""

    for i in employers_list:
        record_to_insert = (i["employer_id"], i['firm'], i["location"])
        cur.execute(postgres_insert_query, record_to_insert)

    conn.commit()
    count = len(employers_list)
    print(f"{count} записей успешно добавлена в таблицу employers")

    cur.close()
    conn.close()


def insert_vacancies(vacancies_list, database_name: str, params: dict):
    """Вставляем вакансии"""
    conn = psycopg2.connect(dbname=database_name, **params)
    conn.autocommit = True
    cur = conn.cursor()

    postgres_insert_query = """INSERT INTO public.vacancies(
	                            id, employer_id, name, job_url, requirement, salary_from, salary_to, currency)
	                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"""

    for i in vacancies_list:
        record_to_insert = (
        i["job_id"], i['employer_id'], i["job_name"], i["job_url"], i["requirement"], i["salary_from"], i["salary_to"],
        i["currency"])
        cur.execute(postgres_insert_query, record_to_insert)

    conn.commit()
    count = len(vacancies_list)
    print(f"{count} записей успешно добавлена в таблицу vacancies\n")

    cur.close()
    conn.close()


def get_selected(database_name: str, params: dict):
    """Получаем список компаний"""
    selected = {}
    conn = psycopg2.connect(dbname=database_name, **params)
    conn.autocommit = True
    cur = conn.cursor()

    query = "SELECT id , name FROM  public.selected"

    cur.execute(query)

    res = cur.fetchall()

    for row in res:
        selected[row[0]] = row[1]

    cur.close()
    conn.close()

    return selected
