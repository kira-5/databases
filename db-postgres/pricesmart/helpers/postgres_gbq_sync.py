# import pandas_gbq
import psycopg2 as ps
from utils.db_conn import postgres_connect, flask_sqlalchemy_connect
import pandas as pd


project_name = 'pricesmart-e1078'
dataset_name = 'carters_product_dev'
table_name = 'item_group_data_clone'

new_query = """
    select * from product_master_h10 as pmh
    left join (
        select * from item_group_master as igm
        join
        item_group_product_mapping as igpm
        on igm.custom_item_group_id = igpm.custom_item_group_id
    ) as ig
    on pmh.product_h10_id = ig.product_h10_id
"""


def get_postgres_item_group_data():
    db_conn_sql = None
    df_item_group_data = None

    db_conn_sql = postgres_connect()

    cursor = db_conn_sql.cursor()
    cursor.execute(new_query)
    records = cursor.fetchall()
    columns_name = [column.name for column in cursor.description]
    df_item_group_data = pd.DataFrame(records, columns=columns_name)
    cursor.close()
    db_conn_sql.close()
    df_item_group_data['sync_status'] = 1
    return df_item_group_data


def get_gbq_item_group_data():
    conn = None
    df = None
    sql_query = "select * from item_group_data"
    try:
        db_conn_sql = flask_sqlalchemy_connect()

        df = pd.read_sql(sql=sql_query, con=db_conn_sql)

    except (Exception, ps.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return df


def sync_item_group_data():
    df_item_group_data = get_postgres_item_group_data()
    if not df_item_group_data['sync_status'].isin([1]).any():
        return False
    postgress_item_group_columns = df_item_group_data.columns.to_list()
    gbq_item_group_columns = get_gbq_item_group_data().columns.to_list()

    unwanted_columns = [postgress_item_group_columns[i] for i in range(
        len(postgress_item_group_columns)) if postgress_item_group_columns[i]
        not in gbq_item_group_columns
    ]

    # Drop unwanted column
    df_item_group_data.drop(unwanted_columns, axis=1, inplace=True)

    # Remove Duplicates Columns
    df_item_group_data = df_item_group_data.loc[
        :,
        ~df_item_group_data.columns.duplicated()
    ].copy()

    # Push dataframe to GBQ
    print(df_item_group_data.head(5))
    db_conn = None
    db_conn_sql = None
    # column_type = {
    #     'empfname': sqlalchemy.types.VARCHAR(255),
    #     'emplname': sqlalchemy.types.VARCHAR(255),
    #     'department': sqlalchemy.types.VARCHAR(255),
    #     'address': sqlalchemy.types.VARCHAR(255),
    #     'gender': sqlalchemy.types.VARCHAR(255)
    # }
    try:
        db_conn_sql = flask_sqlalchemy_connect()
        df_item_group_data.to_sql(name='item_group_data', con=db_conn_sql, if_exists='replace', index=False)

        # For commit
        db_conn = postgres_connect()
        db_conn.commit()
    except (Exception, ps.DatabaseError) as error:
        print(error)
    finally:
        if db_conn is not None and db_conn_sql is not None:
            db_conn.close()
            db_conn_sql.close()
    return True




def update_postgress_sync_status():
    update_query = """
    UPDATE item_group_product_mapping
        SET sync_status = 0
        where sync_status = '1'
    """
    if not sync_item_group_data():
        print("No updation is required!")
        return False

    db_conn = None
    cursor = None

    try:
        db_conn = postgres_connect()
        cursor = db_conn.cursor()
        cursor.execute(update_query)
        db_conn.commit()
        cursor.close()
    except (Exception) as error:
        print(error)
        return False
    finally:
        if db_conn is not None:
            db_conn.close()
    print("Sync Status is updated in postgress: item_group_product_mapping_clone!")
    return True
