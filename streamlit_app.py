import streamlit
import pandas
streamlit.title('My parents new Diner Menu')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 Blue Berry Oatmeal')
streamlit.text('🥗 Spinach Kale Smoothi')
streamlit.text('🐔 Hard-boile Egg')
streamlit.text('🥑 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
