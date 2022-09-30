"""
Insert
"""
import psycopg2 as ps
from db_conn import connect
from utils import queries
import pandas as pd


def single_insertion(emp_info):
    """Insert data"""
    db_conn = None

    n = ','.join(['%s'] * len(emp_info))
    sql_query = queries.INSERT_DATA.format(n)
    try:
        db_conn, db_conn_sql = connect()

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
    """Insert data"""
    n = ','.join(['%s'] * len(emp_info_data))
    sql_query = queries.INSERT_DATA.format(n)
    db_conn = None
    try:
        db_conn, db_conn_sql = connect()

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


def load_df():
    data = {'empid': {0: 1, 1: 2, 2: 3, 3: 4, 4: 6}, 'empfname': {0: 'Manjay', 1: 'Ananya', 2: 'Rohan', 3: 'Sonia', 4: 'Ankit'}, 'emplname': {0: 'Mehra', 1: 'Mishra', 2: 'Diwan', 3: 'Kulkarni', 4: 'Mehra'}, 'department': {
        0: 'HR', 1: 'Admin', 2: 'Account', 3: 'HR', 4: 'Admin'}, 'address': {0: 'Hyderabad(HYD)', 1: 'Delhi(DEL)', 2: 'Mumbai', 3: 'Hyderabaad', 4: 'Delhi'}, 'gender': {0: 'M', 1: 'F', 2: 'M', 3: 'F', 4: 'M'}}
    df = pd.DataFrame(data)
    db_conn = None
    try:
        db_conn, db_conn_sql = connect()
        df.to_sql('employeeinfo', con=db_conn_sql, if_exists='replace', index=False)

        # For commit
        db_conn.commit()
    except (Exception, ps.DatabaseError) as error:
        print(error)
    finally:
        if db_conn is not None:
            db_conn.close()
