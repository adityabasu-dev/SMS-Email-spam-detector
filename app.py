import streamlit as st
import pickle
import nltk
import string
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
tfidf_vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

stemmer = PorterStemmer()  

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        y.append(stemmer.stem(i))  
    return " ".join(y)

st.title("Email/SMS Spam Detector")
user_input = st.text_area("Enter your message:")

if st.button("Predict"):  
    if user_input:
        preprocessed = transform_text(user_input)
        vectorized = tfidf_vectorizer.transform([preprocessed])
        prediction = model.predict(vectorized)[0]
        
        if prediction == 1:
            st.error("Spam")
        else:
            st.success("Not Spam")
    else:
        st.warning("Please enter a message")