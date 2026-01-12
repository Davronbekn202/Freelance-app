import psycopg2
def get_connection():
    return psycopg2.connect(
        dbname="freelance",
        user='postgres',
        password="A0B1D9E2",
        host='localhost',
        port=5432
    )

def table_of_accounts():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts(
    id serial PRIMARY KEY,
    name varchar(50) NOT NULL,
    surname varchar(50),
    email varchar(150) unique not null,
    password varchar(8))""")
    connection.commit()
    cursor.close()
    print("Table created successfully")

def add_account(name,surname,email,password):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO accounts(name,surname,email,password)
    VALUES(%s,%s,%s,%s)
    """,(name,surname,email,password))
    connection.commit()
    cursor.close()
def show_result():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM accounts""")
    row = cursor.fetchall()
    for rows in row:
        print(f"id-{rows[0]}, name-{rows[1]}, surname-{rows[2]}, email-{rows[3]},")


table_of_accounts()
