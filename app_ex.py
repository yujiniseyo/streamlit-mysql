import streamlit as st
import mysql.connector
from mysql.connector import Error


def main() :
    try :
        # 1. 커넥터로부터 커넥션을 받는다
        connection = mysql.connector.connect(
            host = 'database-1.caig2vten5jf.ap-northeast-2.rds.amazonaws.com',
            database = 'yhdb',
            user = 'streamlit',
            password = 'yh1234'
        )

        if connection.is_connected() :

            db_info = connection.get_server_info()
            print('MySQL server version : ', db_info)

            # 2. 커서를 가져온다
            cursor = connection.cursor()

            # 3. 우리가 원하는 거 실행 가능
            cursor.execute('select database();')
            
            # 4. 실행 후 커서에서 결과를 빼낸다
            record = cursor.fetchone()
            print('Connected to DB : ', record)

    except Error as e :
        print('DB 관련 에러 발생', e)
    
    finally :
        # 5. 모든 데이터 베이스 실행 명령을 전부 끝냈으면, 커서와 커넥션을 모두 닫아준다
        cursor.close()
        connection.close()
        print('MySQL Connection 종료')




if __name__ == '__main__' :
    main()