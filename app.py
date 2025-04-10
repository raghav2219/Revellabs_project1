from dotenv import load_dotenv
load_dotenv() # Load environment variables from .env file
import os
import streamlit as st
import sqlite3

import google.generativeai as genai

## configure the API key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

## Function to load Google Gemini model and provide sql query as response

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content([prompt[0], question])
    return response.text

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

prompt =[
        """
            You are a SQL expert in converting English questions
            to SQL query! The SQL database has the CustomerData table 
            and has the folowwing columns: CustomerID, Name, Segment, Country, City.
            For example1, How many entries of records are present? the sql
            command will be SELECT COUNT(*) FROM CustomerData; \n
            For example2, How many customers are there in the CustomerData table?
            The sql command will be SELECT COUNT(*) FROM CustomerData; \n   
            For example3, How many customers resides in the city of New York?
            The sql command will be SELECT COUNT(*) FROM CustomerData WHERE City='New York'; \n
            For example4, How many customers are of consumer segment?
            The sql command will be SELECT COUNT(*) FROM CustomerData WHERE Segment='Consumer'; \n
            Also, the sql command should not have ''' in the beginning and end of the command.
        """
        ]

##Streamlit app

st.set_page_config(page_title="Gemini SQL Query Generator", page_icon=":guardsman:", layout="wide")
st.header("Gemini App to Retrieve SQL data")

question = st.text_input("Input: ", key="input")

submit=st.button("Ask the question")

#if submit is clicked
if submit:
    response=get_gemini_response(question, prompt)
    print(response)
    data = read_sql_query(response, 'database.db')
    st.header(f'The SQL query is:- \n {response}')
    for row in data:
        st.subheader(f'The result is:- {row}')