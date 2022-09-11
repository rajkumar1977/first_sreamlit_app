
import streamlit
streamlit.title('My Parents New Healthy Dinner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacoda Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
#import pandas
#my_fruit_list= pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#streamlit.dataframe(my_fruit_list)
import pandas
my_fruit_list= pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#let put picklist
streamlit.multiselect("Pick Some fruits:",list(my_fruit_list.index))
#display table on range
streamlit.dataframe(my_fruit_list)
#let put picklist which you need
#streamlit.multiselect("Pick Some fruits:",list(my_fruit_list.index),['Avacoda','Strawberries'])
