import streamlit as st
import mysql.connector
from mysql.connector import Error
from datetime import datetime, date, time

def main() :

    # title = st.text_input('책 제목을 입력하세요.')
    # author_fname = st.text_input('작가의 이름을 입력하세요.')
    # author_lname = st.text_input('작가의 성을 입력하세요.')
    # released_year = st.number_input('출간년도을 입력하세요.')
    # stock_quantity = st.number_input('수량을 입력하세요.')
    # pages = st.number_input('페이지 수를 입력하세요.')

    # name = st.text_input('이름을 입력하세요.')
    # birthdate = st.date_input('생일을 입력하세요.')
    # birthtime = st.time_input('시간을 입력하세요.')
    # birthdt = datetime.combine(birthdate, birthtime)
    # print(birthdate)
    # print(birthtime)


    if st.button('SAVE') :
        st.text('저장 되었습니다.')


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
                query = '''insert into cats4 (name,age)
                        values(%s, %s);'''
                
                record = [('야옹잉',1), ('나비',5), ('단비',6)]
                # print(datetime.now())

                cursor.executemany(query, record)    
                connection.commit() 
                print('{}개 적용 됨.'.format(cursor.rowcount))

                # 4. 실행 후 커서에서 결과를 빼낸다
                # record = cursor.fetchone()
                # print('Connected to DB : ', record)

        except Error as e :
            print('DB 관련 에러 발생', e)
        
        finally :
            # 5. 모든 데이터 베이스 실행 명령을 전부 끝냈으면, 커서와 커넥션을 모두 닫아준다
            cursor.close()
            connection.close()
            print('MySQL Connection 종료')




if __name__ == '__main__' :
    main()