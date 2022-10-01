"""Table"""
from crud_operation.select import get_dataframe, get_tuples
from crud_operation.create_table import create_tables
from crud_operation.insert_data import single_insertion, multiple_insertion, \
    insert_dataframe

if __name__ == '__main__':

    create_tables()

    emp_info = [(1, 'Sanjay', 'Mehra', 'HR', 'Hyderabad(HYD)', 'M')]
    print(single_insertion(emp_info))
    emp_info_data = [
        (2, 'Ananya', 'Mishra', 'Admin', 'Delhi(DEL)', 'F'),
        (3, 'Rohan', 'Diwan', 'Account', 'Mumbai', 'M'),
        (4, 'Sonia', 'Kulkarni', 'HR', 'Hyderabaad', 'F'),
        (5, 'Ankit', 'Mehra', 'Admin', 'Delhi', 'M')
    ]
    print(multiple_insertion(emp_info_data))
    print(insert_dataframe())

    print(get_tuples())
    print(get_dataframe())
