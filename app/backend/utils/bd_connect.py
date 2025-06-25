import mysql.connector 

def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="150924",
        database="banco"
    )
    return connection


class BD_execute():
    @staticmethod
    def execute_comand(comand, *args):
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(comand, args)
        result = cursor.fetchall()
        cursor.close()
        connection.close()
        if result:
            return result
        return None
        