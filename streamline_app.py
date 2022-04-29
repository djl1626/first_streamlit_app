import streamlit
import pandas as pd
fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruit_list = fruit_list.set_index('Fruit')

streamlit.title("My Parents New Healthy Diner")
streamlit.header("Breakfast Menu")
streamlit.text("🥣 Omega 3 & Blueberry Oatmeal")
streamlit.text("🥗 Kale, Spinach, & Rocket Smoothie")
streamlit.text("🐔 Hard-boiled Free-range Egg")
streamlit.text("🥑🍞 Avocado Toast")
streamlit.header("🍌🥭 Build Your Own Fruit Smoothie 🥝🍇")
fruits_selected = streamlit.multiselect("Pick some fruits:", list(fruit_list.index), ['Avocado', 'Strawberries'])
streamlit.dataframe(fruit_list.loc[fruits_selected])
