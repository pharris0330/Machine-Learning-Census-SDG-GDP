import streamlit as st
import pickle
import numpy as np

st.title('GDP predictor')

with open('Data/pipe.pkl', 'rb') as pickle_in:
    pipe = pickle.load(pickle_in)

user_input = st.number_input(min_value=0, label='Education attainment')

user_input = np.array(user_input).reshape(-1, 1)
pred = pipe.predict(user_input)[0]

st.write("""
# GDP level
""")
st.write(pred)