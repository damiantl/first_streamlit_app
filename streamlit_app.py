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

# Read the data from source into a pandas dataframe
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# Set the index
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the option they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show  = my_fruit_list.loc[fruits_selected]

# Display the table on the page
streamlit.dataframe(fruits_to_show)

#******************************
# Call API from Streamlit
#******************************

# Add function
def get_fruityvice_data(this_fruit_choice):
  # Inside the function we include the get request and the normalization of the JSON, but not the dataframe visualization of streamlit
  # GET request
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  # JSON normalization using pandas
  fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

# Including Try/Except with nested If/Else
# Write new header
streamlit.header("Fruityvice Fruit Advice!")

# Add entry text box by the user on Streamlit app new box
try:
  fruit_choice = streamlit.text_input("What fruit would you like information about?")
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    # Conversion to dataframe for visualization purposes on Streamlit app
    streamlit.dataframe(back_from_function)

except URLError as e:
  streamlit.error()
