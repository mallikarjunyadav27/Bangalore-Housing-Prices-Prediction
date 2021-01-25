import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import pickle
import numpy as np

from PIL import Image

pickle_in = open('model_pickel','rb')
classifier = pickle.load(pickle_in)

def Welcome():
    return 'WELCOME ALL!'

def predict_price(location,sqft,bath,bhk):    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: location
        in: query
        type: text
        required: true
      - name: sqft
        in: query
        type: number
        required: true
      - name: bath
        in: query
        type: number
        required: true
      - name: bhk
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    #loc_index = np.where(X.columns==location)[0][0]

    x = np.zeros(243)
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    #if loc_index >= 0:
        #   x[loc_index] = 1

    return classifier.predict([x])[0]

def main():
    st.title("Bangalore House Rate Prediction")
    html_temp = """
    <h2 style="color:black;text-align:left;"> Streamlit House prediction ML App </h2>
    """

    st.markdown(html_temp,unsafe_allow_html=True)
    st.subheader('Please enter the required details:')
    location = st.text_input("Location","")
    sqft = st.text_input("Sq-ft area","")
    bath = st.text_input("Number of Bathroom","")
    bhk = st.text_input("Number of BHK","")

    result=""

    if st.button("House Price in Lakhs"):
        result=predict_price(location,sqft,bath,bhk)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Please find the code at")
        st.text("https://github.com/Lokeshrathi/Bangalore-house-s-rate")

if __name__=='__main__':
    main()
    
