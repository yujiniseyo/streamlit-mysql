import streamlit as st
import mysql.connector
import numpy as np
import pandas as pd
import json
from mysql.connector import Error

def my_sql_select() :

    col_list = ['title', 'author_fname', 'author_fname', 'released_year', 'stock_quantity', 'pages']
    
    selected_col_list = st.multiselect('컬럼을 선택하세요', col_list)

    if len(selected_col_list) == 0 :
        query = """ select * from books; """
    
    else :
        col_str = ', '.join(selected_col_list)
        # st.write(col_str)
        query = " select book_id, " + col_str + ' from books;'
        # st.write(query)
    
    # st.write(query)

    try :
        # 1. 커넥터로부터 커넥션을 받는다.
        connection = mysql.connector.connect(
            host = 'database-1.caig2vten5jf.ap-northeast-2.rds.amazonaws.com',
            database = 'yhdb',
            user = 'streamlit',
            password = 'yh1234'
        )

        if connection.is_connected() :
            cursor = connection.cursor(dictionary = True)
            
            # 2. 쿼리 만들어서 실행
            cursor.execute(query)

            # 3. select 이므로, fetchall 해야함
            results = cursor.fetchall()

            # 파이썬의 리스트 + 딕셔너리 조합을 json 형식으로 바꾸는 것
            json_results = json.dumps(results)

            # 판다스의 데이터프레임으로 읽기
            df = pd.read_json(json_results)
            
            st.dataframe(df)
            

    except Error as e :
            print('디비 관련 에러 발생', e)
        
    finally :
        # 5. 모든 데이터베이스 실행 명령을 전부 끝냈으면, 커서와 커넥션을 모두 닫아준다.
        cursor.close()
        connection.close()
        print('MySQL 커넥션 종료')