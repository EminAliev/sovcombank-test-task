from django.db import connection


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def count_data():
    """
    Количество заявок в каждом месяце
    """
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT strftime("%Y-%m", date) as month, count(*) as count
            FROM table_data
            group by month
            """
        )
        result = dictfetchall(cursor)
    return result


def last_data():
    """
    Последнюю заявку по клиенту
    """
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT id, MAX(date) as date, phone_number, product, solution
             FROM table_data
            """
        )
        result = dictfetchall(cursor)
    return result


def client_approved():
    """
    Клиенты которые завели заявки на другой продукт после одобрения
    """
    with connection.cursor() as cursor:
        cursor.execute(
            """
           WITH approved_data as (
                SELECT * 
                FROM table_data
                WHERE solution = 'approved'
                )
            SELECT * 
            FROM table_data JOIN approved_data
            WHERE table_data.phone_number = approved_data.phone_number AND table_data.id > approved_data.id AND table_data.product != approved_data.product
            """
        )
        result = dictfetchall(cursor)
    return result
