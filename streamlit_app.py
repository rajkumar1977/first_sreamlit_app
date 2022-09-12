
import streamlit
streamlit.title('My Parents New Healthy Dinner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacoda Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')




streamlit.header("Fruityvice Fruit Advice!")

#let put picklist
import pandas
fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruits_selected=streamlit.multiselect("Pick Some fruits:",list(my_fruit_list.index),['Avacoda','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
#display table on range




import snowflake.connector
