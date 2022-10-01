"""
Insert
"""
import psycopg2 as ps
from utils.db_conn import postgres_connect, flask_sqlalchemy_connect
from utils import queries
import pandas as pd
import sqlalchemy

def single_insertion(emp_info):
    db_conn = None

    n = ','.join(['%s'] * len(emp_info))
    sql_query = queries.INSERT_DATA.format(n)
    try:
        db_conn = postgres_connect()

        cur = db_conn.cursor()

        cur.execute(sql_query, emp_info)

        db_conn.commit()

        print('Single Insertion Successfull!')

        cur.close()
    except (Exception, ps.DatabaseError) as error:
        print(error)
    finally:
        if db_conn is not None:
            db_conn.close()
    return


def multiple_insertion(emp_info_data):
    n = ','.join(['%s'] * len(emp_info_data))
    sql_query = queries.INSERT_DATA.format(n)
    db_conn = None
    try:
        db_conn = postgres_connect()

        cur = db_conn.cursor()

        cur.execute(sql_query, emp_info_data)

        db_conn.commit()

        print('Multiple Insertion Successfull!')

        cur.close()
    except (Exception, ps.DatabaseError) as error:
        print(error)
    finally:
        if db_conn is not None:
            db_conn.close()


def insert_dataframe():
    data = {'empid': {0: 1, 1: 2, 2: 3, 3: 4, 4: 6}, 'empfname': {0: 'Manjay', 1: 'Ananya', 2: 'Rohan', 3: 'Sonia', 4: 'Ankit'}, 'emplname': {0: 'Mehra', 1: 'Mishra', 2: 'Diwan', 3: 'Kulkarni', 4: 'Mehra'}, 'department': {
        0: 'HR', 1: 'Admin', 2: 'Account', 3: 'HR', 4: 'Admin'}, 'address': {0: 'Hyderabad(HYD)', 1: 'Delhi(DEL)', 2: 'Mumbai', 3: 'Hyderabaad', 4: 'Delhi'}, 'gender': {0: 'M', 1: 'F', 2: 'M', 3: 'F', 4: 'M'}}
    df = pd.DataFrame(data)
    db_conn = None
    db_conn_sql = None
    column_type = {
        'empfname': sqlalchemy.types.VARCHAR(255),
        'emplname': sqlalchemy.types.VARCHAR(255),
        'department': sqlalchemy.types.VARCHAR(255),
        'address': sqlalchemy.types.VARCHAR(255),
        'gender': sqlalchemy.types.VARCHAR(255)
    }
    try:
        db_conn_sql = flask_sqlalchemy_connect()
        df.to_sql(name='employee_info_df', con=db_conn_sql,
                  if_exists='replace', index=False, dtype=column_type)

        # For commit
        db_conn = postgres_connect()
        db_conn.commit()
    except (Exception, ps.DatabaseError) as error:
        print(error)
    finally:
        if db_conn is not None and db_conn_sql is not None:
            db_conn.close()
            db_conn_sql.close()
