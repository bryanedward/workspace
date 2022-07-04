import psycopg2

if __name__ == '__main__':
       # Connect to your postgres DB
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="postgres"
    )
    # Open a cursor to perform database operations
    cur = conn.cursor()
    cur.execute("SELECT * FROM clientes")
    records = cur.fetchall()
    print(records)
