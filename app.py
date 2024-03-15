import pickle 
import time
import streamlit as st

prediction_model = pickle.load(open('placement_model.sav', 'rb'))

st.title("Placement Prediction Model")

col1, col2 = st.columns(2)

with col1:
    cgpa = st.number_input('Enter your CGPA:')
with col2:
    q1 = st.number_input('How good are you at solving puzzles? (1-5):')
with col1:
    q2 = st.number_input('How well do you understand abstract concepts? (1-5):')
with col2:
    q3 = st.number_input('"How fast can you learn new things? (1-5):')
with col1:
    q4 = st.number_input('How strong is your memory? (1-5):')
with col2:
    q5 = st.number_input('How logical are you in problem-solving? (1-5):')
# with col1:
    # iq = st.text_input('Enter your IQ level:')

iq= ((q1 + q2 + q3 + q4 + q5) / 5)
print ("Your IQ level is :",iq)

if st.button('Submit'):
    input_data = [cgpa, iq]
    input_data = [float(x) for x in input_data]
    
    prediction = prediction_model.predict([input_data] )
    
    if prediction >= 1:
        with st.spinner('Loading...'):
            time.sleep(3)
            
        st.success("Congratulations! You got placement." , icon="☑️")
    else:
        st.error("Sorry, you didn't get placement.", icon="🚨")

    st.write("Prediction:", prediction)