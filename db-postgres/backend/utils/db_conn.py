import urllib
import sys
import psycopg2 as ps

from utils.config import env_config
from sqlalchemy import create_engine


environment, config = env_config()
ps_database = config.get(environment, 'database')
ps_user = config.get(environment, 'user')
ps_password = config.get(environment, 'password')
ps_host = config.get(environment, 'host')
ps_port = config.get(environment, 'port')


def postgres_connect():
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
        print(error)
        sys.exit(1)

    return dbConnection


def flask_sqlalchemy_connect():
    """Using Flask-SQLAlchemy"""
    dbConnection_sql = None
    password = urllib.parse.quote(ps_password)
    # ps_url = f"postgresql+psycopg2://{ps_user}:password@{ps_host}:{ps_port}/{ps_database}?password={ps_password}"
    ps_url = f"postgresql+psycopg2://{ps_user}:{password}@{ps_host}:{ps_port}/{ps_database}"
    try:
        alchemyEngine = create_engine(
            ps_url,
            pool_recycle=3600
        )
        dbConnection_sql = alchemyEngine.connect()
    except (ps.DatabaseError) as error:
        print(error)
        sys.exit(1)

    return dbConnection_sql
