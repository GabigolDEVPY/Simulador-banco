import mysql.connector 

def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Gabrielrochadias12",
        database="banco"
    )
    return connection


class BD_execute():
    @staticmethod
    def execute_comand(comand, *args):
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(comand, (args))
        rows = cursor.rowcount
        result = cursor.fetchall()
        connection.commit()
        cursor.close()
        connection.close()
        if result:
            return result
        if rows:
            return rows
        return None
        