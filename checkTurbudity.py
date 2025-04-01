import streamlit as st
import mysql.connector
import pandas as pd
import time

# Function to fetch turbidity data
def get_turbidity_data():
    try:
        conn = mysql.connector.connect(
            host="82.180.143.66",
            user="u263681140_students1",
            password="testStudents@123",
            database="u263681140_students1"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT id, value, timestamp FROM Turbudity WHERE id = 1 ORDER BY timestamp DESC LIMIT 10")
        data = cursor.fetchall()
        conn.close()
        return pd.DataFrame(data, columns=["ID", "Turbidity Value", "Timestamp"])
    except Exception as e:
        st.error(f"Database connection failed: {e}")
        return pd.DataFrame()

# Streamlit Dashboard
st.title("🌊 Turbidity Monitoring Dashboard")
st.write("Displaying recent turbidity readings (Auto-refreshes every 5 seconds)")

while True:
    data = get_turbidity_data()

    if not data.empty:
        # Apply color coding for turbidity levels
        def highlight_values(val):
            if val < 5:
                color = "green"  # Low turbidity
            elif 5 <= val < 10:
                color = "yellow"  # Moderate turbidity
            else:
                color = "red"  # High turbidity
            return f'background-color: {color}; color: white'

        # Display the data in a color-coded table
        st.dataframe(data.style.applymap(highlight_values, subset=["Turbidity Value"]))

        # Plot a line chart for turbidity trends
        st.line_chart(data.set_index("Timestamp")["Turbidity Value"])
    
    else:
        st.write("No data available.")

    time.sleep(5)  # Auto-refresh every 5 seconds
    st.experimental_rerun()
