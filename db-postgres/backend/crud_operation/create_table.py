import psycopg2 as ps
from utils.db_conn import postgres_connect
from utils import queries


def create_tables():
    """ create tables in the PostgreSQL database"""
    query = queries.CREATE_TABLE
    db_conn = None
    try:
        db_conn = postgres_connect()
        cur = db_conn.cursor()

        for command in query:
            cur.execute(command)

        cur.close()
        db_conn.commit()
    except (Exception, ps.DatabaseError) as error:
        print(error)
    finally:
        if db_conn is not None:
            db_conn.close()

    return
