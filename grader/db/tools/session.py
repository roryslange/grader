import psycopg2

def getConn():
    try:
        return psycopg2.connect(
            database="mydb",
            user="myuser",
            password="mypass",
            host="localhost",  # e.g., "localhost" or an IP address
            port="5432"       # default PostgreSQL port
        )
    except psycopg2.Error as e:
        print(f"Error connecting to PostgreSQL: {e}")