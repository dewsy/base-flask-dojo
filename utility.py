import database_common


@database_common.connection_handler
def get_first_names(cursor):
    cursor.execute("""
                    SELECT first_name, id from applicants
                   """)
    first_names = cursor.fetchall()
    return first_names