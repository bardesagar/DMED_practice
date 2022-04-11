
from flask import Flask,request #import flask
import streamlit as st ### 

def hello():

    try:
        st.title("Learning Streamlit")
        stu_name =  st.text_input("StudnetName")
        numb = st.text_input("RollNo")
        result =  f"Student name is {stu_name} and Roll no is {numb}"
        if st.button("Print Output"):
            st.success(result) 
    except Exception as e:
        return f"Error occured with message : {e}"
    

if __name__ == "__main__":
    hello()