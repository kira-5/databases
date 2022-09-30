"""Table"""
from utils.create_table import create_tables
from utils.insert_data import single_insertion, multiple_insertion,load_df
from utils.select import get_data
from utils.gbq_conn import log_in
from db_conn import connect
# from auth import authenticate

if __name__ == '__main__':
    # create_tables()
    # emp_info = [(1, 'Sanjay', 'Mehra', 'HR', 'Hyderabad(HYD)', 'M')]
    # print(single_insertion(emp_info))
    # emp_info_data = [
    #     (2, 'Ananya', 'Mishra', 'Admin', 'Delhi(DEL)', 'F'),
    #     (3, 'Rohan', 'Diwan', 'Account', 'Mumbai', 'M'),
    #     (4, 'Sonia', 'Kulkarni', 'HR', 'Hyderabaad', 'F'),
    #     (5, 'Ankit', 'Mehra', 'Admin', 'Delhi', 'M')
    # ]
    # print(multiple_insertion(emp_info_data))
    
    # print(connect())
    print(load_df())
    
    
