from transformers import pipeline
import streamlit as st

def analyze_sentiment(text):
    sentiment_pipeline = pipeline("sentiment-analysis")
    result = sentiment_pipeline(text)[0]
    return result['label'], result['score']

# Streamlit app code (add this)
st.title("Sentiment Analysis App")
user_input = st.text_area("Enter text for sentiment analysis:")
if st.button("Analyze"):
    if user_input:
        sentiment, score = analyze_sentiment(user_input)
        st.write(f"Sentiment: {sentiment}")
        st.write(f"Confidence: {score:.2f}")
    else:
        st.write("Please enter some text to analyze.")

