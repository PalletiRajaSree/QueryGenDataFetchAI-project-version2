from dotenv import load_dotenv
load_dotenv()  ##Load all the environment variables from the .env file
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

##configure our API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

##create a function to load google gemini model and provide query as response
def get_gemini_response(question,prompt):
    model = genai.GenerativeModel('gemini-3.8-flash')
    response=model.generate_content([prompt,question])
    return response.text

##function to retrive sql query result from database
def read_sql_query(sql,db):
    connection = sqlite3.connect('student.db')
    cursor = connection.cursor()
    cursor.execute(sql)
    data=cursor.fetchall()

    connection.commit()
    connection.close()
    for row in data:
        print(row)
    print(data)
    return data

prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION AND MARKS \n\nFor example,\nExample 1 - How many entries of records are present?,
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?,
    the SQL command will be something like this SELECT * FROM STUDENT
    where CLASS="10th" ;
    also the sql code should not have ``` in beginning or end and sql word in
    """
]


##STREAMLIT UI
st.set_page_config(page_title="QueryGen", page_icon=":guardsman:", layout="wide")
st.title("QueryGen - English to SQL Query Generator")
st.header("This is a simple app that converts English questions to SQL query using Google Gemini API and executes the query on a SQLite database.")
question=st.text_input("Enter your question here")
submit=st.button("Submit")

if submit:
    if question:
        response=get_gemini_response(question,prompt[0])
        print("Generated SQL query is: ",response)
        st.subheader("Generated SQL query is: ")
        st.header(response)
        data=read_sql_query(response,'student.db')
        st.subheader("Query Result is: ")
        for row in data:
            st.header(row)






