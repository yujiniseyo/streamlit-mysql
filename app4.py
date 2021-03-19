import streamlit as st
import mysql.connector
import numpy as np
import pandas as pd
from mysql.connector import Error
from my_sql_select import my_sql_select
# from my_sql_lnsert import my_sql_insert
# from my_sql_update import my_sql_update
# from my_sql_delete import my_sql_delete

def main() :

    menu = ['Select', 'Insert', 'Update', 'Delete']
    choice = st.sidebar.selectbox('MENU', menu)

    if choice == 'Select' :
        my_sql_select()

    # elif choice == 'Insert' :
    #     my_sql_insert()

    # elif choice == 'Update' :
    #     my_sql_update()

    # elif choice == 'Delete' :
    #     my_sql_delete()

if __name__ == '__main__' :
    main()