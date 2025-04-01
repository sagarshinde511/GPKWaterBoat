import streamlit as st
import mysql.connector
import time

# Function to fetch turbidity value
def get_turbidity_value():
    try:
        conn = mysql.connector.connect(
            host="82.180.143.66",
            user="u263681140_students1",
            password="testStudents@123",
            database="u263681140_students1"
        )
        cursor = conn.cursor()
        
        # Fetch the latest turbidity value for id = 1
        cursor.execute("SELECT value FROM Turbudity WHERE id = 1 ORDER BY id DESC LIMIT 1")
        data = cursor.fetchone()
        conn.close()

        return data[0] if data else "No data available"
    except Exception as e:
        st.error(f"Database connection failed: {e}")
        return "Error"

# Streamlit Dashboard
st.title("🌊 Turbidity Monitoring")
st.write("Live turbidity reading (Auto-refreshes every 5 seconds)")

placeholder = st.empty()

while True:
    turbidity_value = get_turbidity_value()
    
    with placeholder.container():
        st.subheader(f"🌡️ Current Turbidity: **{turbidity_value}**")

    time.sleep(5)
    st.rerun()
