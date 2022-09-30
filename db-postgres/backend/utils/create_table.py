""" create tables in the PostgreSQL database"""
import psycopg2 as ps
from db_conn import connect
from utils import queries


def create_tables():
    """ create tables in the PostgreSQL database"""
    query = queries.CREATE_TABLE
    conn = None
    try:
        conn = connect()
        cur = conn.cursor()

        for command in query:
            cur.execute(command)
        print('Table Created!')

        cur.close()
        conn.commit()
    except (Exception, ps.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return
