from sqlalchemy import create_engine
import psycopg2 

conn = psycopg2.connect(
    host = "localhost",
    database="covid",
    user="postgres",
    password="admin",
    port="5432"
)

def test_connection():

    with conn.cursor() as curs:

        try:
            curs.execute("select version()")
            single_row = curs.fetchone()
            print(f"{single_row}")
        except:
            print("Completed attempt")

# test_connection()

def test_connection_2():

    engine = create_engine(
        'postgresql+psycopg2://postgres:admin@localhost:5432/covid') 

    conn = engine.raw_connection()
    cur = conn.cursor()
    output = cur.execute("show tables;")
    print(f"{output}")`

