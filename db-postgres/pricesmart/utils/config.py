"""Config for DB Connection"""
import configparser
import os


def env_config():
    """Read value from envioronmrnt file"""
    config = configparser.RawConfigParser()
    environment = 'postgresql'
    config_file_path = f"{os.getcwd()}/utils/database.ini"
    
    config.read(config_file_path)
    return environment, config
