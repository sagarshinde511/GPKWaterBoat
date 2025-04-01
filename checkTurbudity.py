import streamlit as st
import mysql.connector
import pandas as pd

def get_turbidity_data():
    try:
        conn = mysql.connector.connect(
            host="82.180.143.66",
            user="u263681140_students1",
            password="testStudents@123",
            database="u263681140_students1"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT id, value FROM Turbudity WHERE id = 1")
        data = cursor.fetchall()
        conn.close()
        return pd.DataFrame(data, columns=["ID", "Turbidity Value"])
    except Exception as e:
        st.error(f"Database connection failed: {e}")
        return pd.DataFrame()

st.title("Turbidity Monitoring Dashboard")
st.write("Displaying turbidity reading for ID = 1 from the database.")

data = get_turbidity_data()
if not data.empty:
    st.dataframe(data)
else:
    st.write("No data available.")
