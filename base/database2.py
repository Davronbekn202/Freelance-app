from database import get_connection

def table_of_portfolio():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS portfolio (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) not null ,
    description text not null,
    created_at TIMESTAMP DEFAULT NOW(),
    accounts_id int references accounts(id))''')
    connection.commit()
    cursor.close()
    print("table of portfolio created")
def table_of_job():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS job (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) not null ,
    profession VARCHAR(255) not null,
    expiriance int not null,
    portfolio_id int references portfolio(id) not null,
    accounts_id int references accounts(id)) ''')
    connection.commit()
    cursor.close()
    print("table of job created")
def add_to_job(name,profession,experience,portfolio_id,accounts_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO job (name,profession,experience,portfolio_id,accounts_id)
    VALUES(%s,%s,%s,%s,%s)
    """,(name,profession,experience,portfolio_id,accounts_id))
    connection.commit()
    cursor.close()

def add_to_portfolio(title,description,created_at,accounts_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
    INSERT INTO job (title,description,created_at,accounts_id)
    VALUES(%s,%s,%s,%s)
    """,(title,description,created_at,accounts_id))
    connection.commit()
    cursor.close()


table_of_portfolio()
table_of_job()
