import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

pickle_in = open("model.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(Age,Weight,Height,Neck,Chest,Abdomen,Hip,
Thigh,Knee,Ankle,Biceps,Forearm,Wrist,BMI):
    prediction=classifier.predict(Age,Weight,Height,Neck,Chest,Abdomen,Hip,
    Thigh,Knee,Ankle,Biceps,Forearm,Wrist,BMI)
    print(prediction)
    return prediction

def main():
    st.title("Body Density Predictor")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Age = st.text_input("Age","Type Here")
    Weight = st.text_input("Weight","Type Here")
    Height = st.text_input("Height","Type Here")
    Neck = st.text_input("Neck","Type Here")
    Chest = st.text_input("Chest","Type Here")
    Abdomen = st.text_input("Abdomen","Type Here")
    Hip = st.text_input("Hip","Type Here")
    Thigh = st.text_input("Thigh","Type Here")
    Knee = st.text_input("Knee","Type Here")
    Ankle = st.text_input("Ankle","Type Here")
    Biceps = st.text_input("Biceps","Type Here")
    Forearm = st.text_input("Forearm","Type Here")
    Wrist = st.text_input("Wrist","Type Here")
    BMI = st.text_input("BMI","Type Here")

    result=""
    if st.button("Predict"):
        result=predict_note_authentication(Age,Weight,Height,Neck,Chest,Abdomen,Hip,
Thigh,Knee,Ankle,Biceps,Forearm,Wrist,BMI)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()