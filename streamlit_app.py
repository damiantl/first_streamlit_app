import streamlit
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Import pandas library
#import pandas as pd

# Read the data from source into a pandas dataframe
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# Set the index
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the option they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show  = my_fruit_list.loc[fruits_selected]

# Display the table on the page
#streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)

#******************************
# Call API from Streamlit
#******************************
'''
# New section to display fruityvice api response
#import requests

# Write new header
streamlit.header("Fruityvice Fruit Advice!")

# Add entry text box by the user on Streamlit app new box
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

# GET request
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# JSON normalization using pandas
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())

# Conversion to dataframe for visualization purposes on Streamlit app
streamlit.dataframe(fruityvice_normalized)

# Stop running everything past this point while we troubleshoot
streamlit.stop()

# Import Snowflake connector
#import snowflake.connector

# Connect to Snowflake from Streamlit
#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_data_row = my_cur.fetchone()
#streamlit.text("Hello from Snowflake:")
#streamlit.text(my_data_row)

# Query some data from Snowflake table
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.text("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

# Addition of a second entry box
add_my_fruit = streamlit.text_input("What fruit would you like to add?", 'jackfruit')
streamlit.write('Thanks for adding ' + add_my_fruit)

# Adding rows to Snowflake table
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("insert into fruit_load_list values ('from streamlit')")

# Import URLError package
#from urllib.error import URLError
'''
# Including Try/Except with nested If/Else
# Write new header
streamlit.header("Fruityvice Fruit Advice!")

# Add entry text box by the user on Streamlit app new box
try:
  fruit_choice = streamlit.text_input("What fruit would you like information about?")
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    # GET request
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    # JSON normalization using pandas
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    # Conversion to dataframe for visualization purposes on Streamlit app
    streamlit.dataframe(fruityvice_normalized)

except URLError as e:
  streamlit.error()
