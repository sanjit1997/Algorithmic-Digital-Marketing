import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords 
from nltk.tokenize import WordPunctTokenizer


import string
import re
import pickle
import nltk
import streamlit as st
nltk.download('stopwords')

business_df = pd.read_csv('data/yelp_business_new.csv')

f = open('./recommendation_model/recommendation.pkl', 'rb')
P, Q, userid_vectorizer = pickle.load(f), pickle.load(f), pickle.load(f)

def clean_text(text):
    text = text.translate(string.punctuation)
    
    ## Convert words to lower case and split them
    text = text.lower().split()
    
    ## Remove stop words
    stops = set(stopwords.words("english"))
    text = [w for w in text if not w in stops and len(w) >= 3]
    
    text = " ".join(text)
    
    # Clean the text
    text = re.sub(r"[^A-Za-z0-9^,!.\/'+-=]", " ", text)
    text = re.sub(r"what's", "what is ", text)
    text = re.sub(r"\'s", " ", text)
    text = re.sub(r"\'ve", " have ", text)
    text = re.sub(r"n't", " not ", text)
    text = re.sub(r"i'm", "i am ", text)
    text = re.sub(r"\'re", " are ", text)
    text = re.sub(r"\'d", " would ", text)
    text = re.sub(r"\'ll", " will ", text)
    text = re.sub(r",", " ", text)
    text = re.sub(r"\.", " ", text)
    text = re.sub(r"!", " ! ", text)
    text = re.sub(r"\/", " ", text)
    text = re.sub(r"\^", " ^ ", text)
    text = re.sub(r"\+", " + ", text)
    text = re.sub(r"\-", " - ", text)
    text = re.sub(r"\=", " = ", text)
    text = re.sub(r"'", " ", text)
    text = re.sub(r"(\d+)(k)", r"\g<1>000", text)
    text = re.sub(r":", " : ", text)
    text = re.sub(r" e g ", " eg ", text)
    text = re.sub(r" b g ", " bg ", text)
    text = re.sub(r" u s ", " american ", text)
    text = re.sub(r"\0s", "0", text)
    text = re.sub(r" 9 11 ", "911", text)
    text = re.sub(r"e - mail", "email", text)
    text = re.sub(r"j k", "jk", text)
    text = re.sub(r"\s{2,}", " ", text)    
    return text


def recommend_func():
	st.text("Please enter your thoughts...!")
	title = st.text_input('')
	if title:

		# print("title ===> ",title)
		sentence = title
		test_df = pd.DataFrame([sentence], columns=['text'])
		test_df['text'] = test_df['text'].apply(clean_text)
		test_vectors = userid_vectorizer.transform(test_df['text'])
		test_v_df = pd.DataFrame(test_vectors.toarray(), index=test_df.index,
		                         columns=userid_vectorizer.get_feature_names())

		y_pred = []
		for key, row in test_v_df.iterrows():
		    predictItemRating=pd.DataFrame(np.dot(row,Q.T),index=Q.index,columns=['Rating'])
		    topRecommendations=pd.DataFrame.sort_values(predictItemRating,['Rating'],ascending=[0])[:1]
		    y_pred.append(topRecommendations.index[0])

		# print("y_pred==",y_pred)
		st.text("Here you go ..., the restaurant recommended for you is")
		st.text("")
		for i, row in business_df.iterrows():
			if row["business_id"] == y_pred[0]:
				st.text("Restaurant Name == "+ row["name"])
				st.text("Street == "+row["address"])
				st.text("City == "+row["city"])
				st.text("Category == "+row["categories"])
				st.text("Rating  == "+str(row["stars"]))


