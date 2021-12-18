import pandas as pd
import streamlit as st
import os

def eda():

	df = pd.read_csv('data/yelp_business_new.csv')

	cities_list = df.city.unique()

	option = st.selectbox('Select Your City', tuple(cities_list))

	restaurant_list = []
	for i, row in df.iterrows():
		if row["city"] == option:
			restaurant_list.append(row["name"])

	title = st.selectbox('Select Your Restaurant', tuple(restaurant_list))

	location = (df.at[df['name'].eq(title).idxmax(), 'address'])
	rating = (df.at[df['name'].eq(title).idxmax(), 'stars'])
	categories = (df.at[df['name'].eq(title).idxmax(), 'categories'])

	st.text("Location: "+location)
	st.text("Rating: "+str(rating))
	st.text("Description: "+categories)