import sqlite3
import pandas as pd
import streamlit as st

@st.cache_resource
def db_creator(upload_file,flag = False ):
    if flag:
        data = pd.read_csv(upload_file)
        file_name = upload_file.name
    else:
        data = pd.read_csv(f"./data/{upload_file}")
        file_name = upload_file

    try:
        conn = sqlite3.connect(f"./data/{file_name[:-4]}.db")
        # cursor = conn.cursor()
        data.to_sql(name=file_name[:-4].replace("-","").replace("_",""),con=conn,if_exists="replace",index=False)
        print("Data converted to SQL successfully")
        conn.commit()
        conn.close()
    except Exception as err:
        print(err)
        st.write("Not able to load csv!!")
        




# ## Connect to Sqlite

# connection = sqlite3.connect('./data/student.db')

# # Create cursor obj to insert record, create table, retrieve
# cursor = connection.cursor()

# ## Create table 

# table_info = """
# Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT); 
# """

# cursor.execute(table_info)


# ## insert more records 

# cursor.execute('''Insert Into STUDENT values('Krish','Data Science','A',90)''')
# cursor.execute('''Insert Into STUDENT values('Salman','CS','B',60)''')
# cursor.execute('''Insert Into STUDENT values('Sunny','Data Science','D',70)''')
# cursor.execute('''Insert Into STUDENT values('Sudhanshu','Data Science','C',34)''')
# cursor.execute('''Insert Into STUDENT values('swapnil','Data Science','F',56)''')
# cursor.execute('''Insert Into STUDENT values('Raviraj','Data Science','F',25)''')
# cursor.execute('''Insert Into STUDENT values('Gaurav','Data Science','A',56)''')
# cursor.execute('''Insert Into STUDENT values('Tarun','AI','D',79)''')
# cursor.execute('''Insert Into STUDENT values('Jay','AI','C',32)''')
# cursor.execute('''Insert Into STUDENT values('Sanjay','IT','C',34)''')
# cursor.execute('''Insert Into STUDENT values('Vishal','CS','D',66)''')
# cursor.execute('''Insert Into STUDENT values('Ravi','ENTC','F',93)''')
# cursor.execute('''Insert Into STUDENT values('Riya','Instrumentation','B',39)''')
# cursor.execute('''Insert Into STUDENT values('Hardik','Chemical','D',10)''')
# cursor.execute('''Insert Into STUDENT values('Suman','Chemical','C',47)''')
# cursor.execute('''Insert Into STUDENT values('Raahish','MBA','B',77)''')
# cursor.execute('''Insert Into STUDENT values('Grace','MBA','A',10)''')


# print("The Data inserted are!")

# data = cursor.execute('''SELECT * FROM STUDENT''')

# # for row in data:
# #     print(row)


# connection.commit()
# connection.close()