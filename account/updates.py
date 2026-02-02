from base.database import get_connection

def update_name(name,id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
    UPDATE accounts SET name=%s WHERE id=%s
    ''',(name,id))
    connection.commit()
    connection.close()

def update_surname(surname,id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
    UPDATE accounts SET surname=%s WHERE id=%s
    ''',(surname,id))
    connection.commit()
    connection.close()

def update_email(email,id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
    UPDATE accounts SET email=%s WHERE id=%s
    ''',(email,id))
    connection.commit()
    connection.close()

def update_password(password,id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''
    UPDATE accounts SET password=%s WHERE id=%s
    ''',(password,id))
    connection.commit()
    connection.close()

