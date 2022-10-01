# df = pd.read_sql_query('select * from "Stat_Table"',con=engine)
import psycopg2 as ps
from utils.db_conn import postgres_connect, flask_sqlalchemy_connect
from utils import queries
import pandas as pd


def get_tuples():
    db_conn = None
    cursor = None
    emp_records = None
    sql_query = queries.SELECT_ALL.format('employee_info')
    try:
        db_conn = postgres_connect()

        cursor = db_conn.cursor()
        cursor.execute(sql_query)

        """
            cursor.fetchall() to fetch all rows.
            cursor.fetchone() to fetch single row.
            cursor.fetchmany(SIZE) to fetch limited rows

        """
        emp_records = cursor.fetchall()
        db_conn.commit()

    except (Exception, ps.DatabaseError) as error:
        print(error)
    finally:
        if db_conn is not None:
            cursor.close()
            db_conn.close()

    return emp_records


def get_dataframe():
    conn = None
    df = None
    sql_query = queries.SELECT_ALL.format('employee_info_df')
    try:
        db_conn_sql = flask_sqlalchemy_connect()

        df = pd.read_sql(sql=sql_query, con=db_conn_sql)

    except (Exception, ps.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return df


def get_csv():
    """
        TODO: Load data from postgres in a CSV File.
    """
    pass
