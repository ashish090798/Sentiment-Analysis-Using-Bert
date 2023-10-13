from transformers import pipeline
import streamlit as st


st.title("Sentiment Analysis Using Bert")
st.header("Please follow the Steps Given below : ")
st.write('1. Please enter the text input')
st.write('2. Please hit the submit button')
st.write('3. Get the output result')

input_data = st.text_input("Enter the text")
if (st.button('Submit')):    
    classifier = pipeline('sentiment-analysis')
    result = classifier(input_data.title())[0]['label']
    if result == 'POSITIVE':
        st.success(result)        
    else:
        st.error(result)
        
st.header('For more such details follow me on https://www.linkedin.com/in/ashishtiwari2114/')
     
    


