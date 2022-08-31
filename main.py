import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

pickle_mod = open("model.pkl","rb")
pickle_trans = open("transformer.pkl", "rb")
classifier=pickle.load(pickle_mod)
transformer = pickle.load(pickle_trans)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(X):
    Y = transformer.transform(X)
    prediction=classifier.predict(Y)
    print(prediction)
    return prediction

def main():
    st.title("Body Density Predictor")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Body Density Predictor ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Age = st.text_input("Age","")
    Neck = st.text_input("Neck","")
    Abdomen = st.text_input("Abdomen","")
    CtoH = st.text_input("Chest to Hip ratio","")
    Thigh = st.text_input("Thigh","")
    Knee = st.text_input("Knee","")
    Ankle = st.text_input("Ankle","")
    Biceps = st.text_input("Biceps","")
    Forearm = st.text_input("Forearm","")
    Wrist = st.text_input("Wrist","")
    bmi = st.text_input("BMI","")

    result=""
    if st.button("Predict"):
        result=predict_note_authentication([[Age,Neck,Abdomen,CtoH,Thigh,Knee,Ankle,Biceps,Forearm,Wrist,bmi]])
        
    st.success('The density is {}'.format(result))

    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()