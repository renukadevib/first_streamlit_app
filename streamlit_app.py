import streamlit
import pandas
import requests
import snowflake.connector
streamlit.title('My parents new Diner Menu')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 Blue Berry Oatmeal')
streamlit.text('🥗 Spinach Kale Smoothi')
streamlit.text('🐔 Hard-boile Egg')
streamlit.text('🥑 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
fruit_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruit_selected]
streamlit.dataframe(fruits_to_show)
streamlit.header('Fruityvice Fruit Choice')
fruit_choice=streamlit.text_input('What fruit information you would like to see?','kiwi')
streamlit.write('The user choice',fruit_choice)
fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
# streamlit.text(fruityvice_response.json())
fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)
my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur=my_cnx.cursor()
my_cur.execute("select CURRENT_USER(),CURRENT_ACCOUNT(),CURRENT_REGION()")
my_data_row=my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
