import streamlit as st
import streamlit as st
import pickle
import numpy as np

# import the model
model = pickle.load(open('model.pkl','rb'))
data = pickle.load(open('data.pkl','rb'))

st.title("Loan Price Predictor")

# gender
gender = st.selectbox('Gender',data['Gender'].unique())

# married_status
married_status = st.selectbox('Married-Status',data['Married'].unique())

#Education
education = st.selectbox('Education',data['Education'].unique())

# Dependents
dependents = st.selectbox('Number of dependents',data['Dependents'].unique())

# Employement
employement = st.selectbox('Employment-Status',data['Self_Employed'].unique())

# Applicant Income
applicant_income= np.log(st.number_input('Income'))

# Loan-amount
loan_amount = np.log(st.number_input('Loan-Amount'))

#Property_area
property = st.selectbox('Property_Area',data['Property_Area'].unique())

# Loan_Amount_Term
loan_term = st.number_input('Loan_Amount_Term')

# Credit history
credit_history = st.number_input('Credit history')

if st.button('Predict'):
    # query
   

    query = np.array([gender,married_status,dependents,education,employement,applicant_income,loan_amount,loan_term,credit_history,property])
    query = query.reshape(1,10)
    result = model.predict(query)[0]
    if result == 0:
        st.subheader('Sorry You are not eligible for this loan')
    else:
        st.subheader('Congratulation! You are eligible for this loan')