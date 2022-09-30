# df = pd.read_sql_query('select * from "Stat_Table"',con=engine)

""" create tables in the PostgreSQL database"""
import psycopg2 as ps
from db_conn import connect
from utils import queries
import pandas as pd


def get_data():
    """ create tables in the PostgreSQL database"""
    conn = None
    df = None
    try:
        conn = connect()

        df = pd.read_sql_query('select * from EmployeeInfo', con=conn)

    except (Exception, ps.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return df
