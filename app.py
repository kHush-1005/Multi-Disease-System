# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 09:57:10 2025

@author: jaydip prajapati
"""
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
# Theme Toggle
st.set_page_config(page_title="Multiple Disease Prediction", layout="wide")

# Shared custom styles (input borders always visible)
base_css = """
    <style>
    input, textarea {
        border: 1px solid #888 !important;
        border-radius: 5px !important;
        padding: 8px !important;
    }
    .stTextInput > div > div > input {
        border: 1px solid #888 !important;
        border-radius: 5px !important;
        padding: 8px !important;
    }
    </style>
"""

# Apply Dark or Light Theme
st.markdown("""
        <style>
        .stApp {
            background-color: #ffffff;
            color: black;
        }
        .css-6qob1r, .css-1d391kg, .css-1v3fvcr {
            background-color: #f0f2f6 !important;
        }
        .stTextInput > div > div > input {
            background-color: #ffffff !important;
            color: #000000 !important;
        }
        .css-1cpxqw2, .css-10trblm {
            color: #000000 !important;
        }
        </style>
    """, unsafe_allow_html=True)

# Always apply base input styles
st.markdown(base_css, unsafe_allow_html=True)


    


# loading the saved model
diabetes_model = pickle.load(open('D:\khushal-55\deploying model\multi diesease model/model_1.sav','rb'))

heart_diesease_model = pickle.load(open('D:\khushal-55\deploying model\multi diesease model/model_2.sav','rb'))

parkinsons_model = pickle.load(open('D:\khushal-55\deploying model\multi diesease model/model_3.sav','rb'))

#sidebar for navigate

with st.sidebar:
    
    selected = option_menu('Multiple Diesease Prediction System',
                           
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],

                           icons = ['activity','heart','person'],
                           
                           default_index = 0)
    # Maker Info BELOW menu
    st.markdown("---")
    st.markdown("### 👨‍💻 Made by: **Khushal Prajapati**")
    st.markdown("**📧 Contact:** [kpraj8423@gmail.com](mailto:kpraj8423@gmail.com)")
    
# Diabetes Prediction page
if(selected == 'Diabetes Prediction'):
    
  #page title
   st.title('Diabetes Prediction using ML')
   
   #getting data from the user
   # creating columns for input fields
   col1,col2,col3 = st.columns(3)
   
   with col1:
      Pregnancies = st.text_input('Number of Pregnancies')
   
   with col2:
      Glucose = st.text_input('Glucose Level')
   
   with col3:
      BloodPressure = st.text_input('BloodPressure value')
   
   with col1:
      SkinThickness = st.text_input('Skin Thickness value')
   
   with col2:
      Insulin = st.text_input('Insulin Level')
   
   with col3:
      BMI = st.text_input('BMI value')
   
   with col1:
      DiabetesPedigreeFunction = st.text_input('Diabetes predigree Function value')
   
   with col2:
     Age = st.text_input('Age of  the Person')
 
    #code for prediction
   diagnosis = ''
    
    #creating a button
   if st.button('Diabetes Test Result'):
      diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
      
      if(diab_prediction[0] == 1):
          diagnosis = 'The Person is Diabetic'
      else:
          diagnosis = 'The Person is Not Diabetic'
          
   st.success(diagnosis)

            
# Heart Diesease page            
if(selected == 'Heart Disease Prediction'):
       
   #page title
   st.title('Heart Disease Prediction using ML') 
   
   #getting data from the user
   # creating columns for input fields
   col1,col2,col3 = st.columns(3)
   
   with col1:
      age = st.text_input('Age of  the Person')
   
   with col2:
      sex = st.text_input('Sex')
   
   with col3:
      cp = st.text_input('Chest pain types')
   
   with col1:
      trestbps = st.text_input('Resting Blood Pressure')
   
   with col2:
      chol = st.text_input('Serum Cholestaral in mg/dl')
   
   with col3:
      fbs = st.text_input('Fasting Blood Suger > 120 mb/dl')
   
   with col1:
      restecg = st.text_input('Resting Electocardiographic results')
   
   with col2:
     thalach = st.text_input('Maximum Heart Rate achieved')
     
   with col3:
     exang = st.text_input('Exercise Induced Angina')
     
   with col1:
     oldpeak = st.text_input('ST depression induced by exerise')
     
   with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
   
   with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
    
   with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    
    # code for Prediction
   heart_diagnosis = ''

    # creating a button for Prediction

   if st.button('Heart Disease Test Result'):
     
      user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
      
      user_input = [float(x) for x in user_input]
      
      heart_prediction = heart_diesease_model.predict([user_input])

      if (heart_prediction[0] == 1):
            heart_diagnosis = 'The person is having heart disease'
      else:
            heart_diagnosis = 'The person does not have any heart disease'

   st.success(heart_diagnosis)
   
# parkinsons Disease page   
if(selected == 'Parkinsons Prediction'):
       
   #page title
   st.title('Parkinsons Prediction using ML') 
         
   col1, col2, col3, col4, col5 = st.columns(5)

   with col1:
       fo = st.text_input('MDVP:Fo(Hz)')

   with col2:
       fhi = st.text_input('MDVP:Fhi(Hz)')

   with col3:
       flo = st.text_input('MDVP:Flo(Hz)')

   with col4:
       Jitter_percent = st.text_input('MDVP:Jitter(%)')

   with col5:
       Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

   with col1:
       RAP = st.text_input('MDVP:RAP')

   with col2:
       PPQ = st.text_input('MDVP:PPQ')

   with col3:
       DDP = st.text_input('Jitter:DDP')

   with col4:
      Shimmer = st.text_input('MDVP:Shimmer')

   with col5:
      Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

   with col1:
      APQ3 = st.text_input('Shimmer:APQ3')

   with col2:
      APQ5 = st.text_input('Shimmer:APQ5')

   with col3:
      APQ = st.text_input('MDVP:APQ')

   with col4:
      DDA = st.text_input('Shimmer:DDA')

   with col5:
      NHR = st.text_input('NHR')

   with col1:
      HNR = st.text_input('HNR')

   with col2:
      RPDE = st.text_input('RPDE')

   with col3:
      DFA = st.text_input('DFA')
   
   with col4:
     spread1 = st.text_input('spread1')

   with col5:
     spread2 = st.text_input('spread2')

   with col1:
     D2 = st.text_input('D2')

   with col2:
     PPE = st.text_input('PPE')
     
    # code for Prediction
   parkinsons_diagnosis = ''

   # creating a button for Prediction    
     
   if st.button("Parkinson's Test Result"):

     user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

     user_input = [float(x) for x in user_input]

     parkinsons_prediction = parkinsons_model.predict([user_input])

     if parkinsons_prediction[0] == 1:
        parkinsons_diagnosis = "The person has Parkinson's disease"
     else:
        parkinsons_diagnosis = "The person does not have Parkinson's disease"

   st.success(parkinsons_diagnosis)  

    