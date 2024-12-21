import json
import streamlit as st
import requests

# Title of the app
st.title('Loan Approval Classification')

# Dictionary to store user inputs
user_options = {}

# Input fields expected by the API
user_options["person_age"] = st.sidebar.slider("Person Age", 20, 144, value=30)

user_options["person_gender"] = st.sidebar.selectbox("Person Gender", ["Male", "Female"])

user_options["person_education"] = st.sidebar.selectbox("Person Education", ["Bachelor", "Associate", "High School", "Master", "Doctorate"])

user_options["person_income"] = st.sidebar.slider("Person Income", 0, 7300000, value=50000)

user_options["person_emp_exp"] = st.sidebar.slider("Employment Experience (Years)", 0, 100, value=5)

user_options["person_home_ownership"] = st.sidebar.selectbox(
    "Home Ownership", ["OWN", "RENT", "MORTGAGE", "OTHER"]
)
user_options["loan_amnt"] = st.sidebar.slider("Loan Amount", 0, 50000, value=350)

user_options["loan_intent"] = st.sidebar.selectbox(
    "Loan Intent", ["EDUCATION", "MEDICAL", "PERSONAL", "VENTURE", "DEBTCONSOLIDATION"]
)
user_options["loan_int_rate"] = st.sidebar.slider("Interest Rate (%)", 2.0, 50.0, value=10.5)
user_options["loan_percent_income"] = st.sidebar.slider(
    "Loan Percent Income (Ratio)", 0.0, 1.0, value=0.2
)
user_options["cb_person_cred_hist_length"] = st.sidebar.slider(
    "Credit History Length (Years)", 0, 50, value=10
)
user_options["credit_score"] = st.sidebar.slider("Credit Score", 300, 900, value=700)

user_options["previous_loan_defaults_on_file"] = st.sidebar.selectbox(
    "Previous Loan Defaults on File?", ["True", "False"]
)

# Display user inputs
st.write("### User Inputs:")
st.json(user_options)

# Button to trigger prediction
if st.button('Predict'):
    # Convert user inputs to JSON format
    data = json.dumps(user_options, indent=2)

    # Send POST request to prediction API and display result
    try:
        response = requests.post('http://165.227.76.151/predict', data=data)
        prediction = response.json()
        st.write("### Prediction Result:")
        st.write(prediction)
    except Exception as e:
        st.error(f"An error occurred: {e}")
