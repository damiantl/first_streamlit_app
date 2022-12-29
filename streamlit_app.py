import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Import pandas library
import pandas as pd

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

# New section to display fruityvice api response
import requests

# Write new header
streamlit.header("Fruityvice Fruit Advice!")

# Add entry text box
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

# GET request
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# JSON normalization using pandas
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())

# Conversion to dataframe for visualization purposes on Streamlit app
streamlit.dataframe(fruityvice_normalized)
