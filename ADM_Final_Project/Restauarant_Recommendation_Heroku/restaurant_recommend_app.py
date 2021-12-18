import streamlit as st
from PIL import Image
from Pages import home,EDA,recommend


st. sidebar.image(Image.open('./images/restaurant_clip_icon.jpg'),use_column_width=200)
st.sidebar.title("Restaurant Recommendation System")


option = st.sidebar.radio(
    'Navigate through various features of the app!',
    ('Home', 'Our List of Restaurants.','Restuarants We Recommend based on your input.')
)

if option == 'Home':
    home.home_func()

if option == 'Our List of Restaurants.':
    EDA.eda()

if option == 'Restuarants We Recommend based on your input.':
    recommend.recommend_func()
