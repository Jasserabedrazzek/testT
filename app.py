import streamlit as st
import sqlite3

# Connect to the database
conn = sqlite3.connect('your_database.db')
c = conn.cursor()

# Query the database for storage and data usage
c.execute("SELECT SUM(storage) FROM your_table")
total_storage = c.fetchone()[0]

c.execute("SELECT SUM(data_usage) FROM your_table")
total_data_usage = c.fetchone()[0]

# Create a Streamlit app
def main():
    st.title("Storage and Data Usage")
    st.write("Total Storage: ", total_storage)
    st.write("Total Data Usage: ", total_data_usage)

if __name__ == "__main__":
    main()
