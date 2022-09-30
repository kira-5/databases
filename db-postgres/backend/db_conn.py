"""Module providingFunction printing python version."""
import psycopg2 as ps
from utils.config import env_config
import sys
from sqlalchemy import create_engine
import pandas as pd


def connect():
    """
    Connection
    """
    environment, config = env_config()
    ps_database = config.get(environment, 'database')
    ps_user = config.get(environment, 'user')
    ps_password = config.get(environment, 'password')
    ps_host = config.get(environment, 'host')
    ps_port = config.get(environment, 'port')
    dbConnection = None
    try:
        print('Connecting to the PostgreSQL database...')
        dbConnection = ps.connect(
            database=ps_database,
            user=ps_user,
            password=ps_password,
            host=ps_host,
            port=ps_port)
        print("Connection Successful!")
    except (ps.DatabaseError) as error:
        print(error, exc_info=True)
        sys.exit(1)

    """Using Flask-SQLAlchemy"""
    ps_url = f"postgresql+psycopg2://{ps_user}:password@{ps_host}:{ps_port}/{ps_database}?password={ps_password}"
    alchemyEngine = create_engine(
        ps_url,
        pool_recycle=3600
    )
    dbConnection_sql = alchemyEngine.connect()
    # dataFrame = pd.read_sql("select * from EmployeeInfo", dbConnection)
    # # pd.set_option('display.expand_frame_repr', False)
    # dbConnection.close()
    # return dataFrame.to_dict()

    return dbConnection, dbConnection_sql


# if __name__ == '__main__':
#     connect()
