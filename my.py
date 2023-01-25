import pandas as pd
import numpy as np
import streamlit as st
import pickle
pipe_t20=pickle.load(open('pipe.pkl', 'rb'))
pipe_odi=pickle.load(open('pipe_odi.pkl', 'rb'))
teams = [
    'Australia',
    'India',
    'Bangladesh',
    'New Zealand',
    'South Africa',
    'England',
    'West Indies',
    'Afghanistan',
    'Pakistan',
    'Sri Lanka'
]
citys = ['Christchurch', 'St Kitts', 'Melbourne', 'St Lucia', 'Canberra',
       'Wellington', 'Mirpur', 'Pune', 'Dubai', 'Ahmedabad',
       'Thiruvananthapuram', 'Lucknow', 'Colombo', 'Cuttack', 'Adelaide',
       'Durban', 'Port Elizabeth', 'Visakhapatnam', 'Auckland', 'Sydney',
       'Delhi', 'Lahore', 'Mount Maunganui', 'Johannesburg', 'Chennai',
       'Cape Town', 'Dominica', 'Hambantota', 'Trinidad', 'Birmingham',
       'Harare', 'Nelson', 'Pallekele', 'Chester-le-Street', 'Kolkata',
       'Abu Dhabi', 'Rajkot', 'Chandigarh', 'Bristol', 'London', 'Guyana',
       'Napier', 'Ranchi', 'Kanpur', 'Chittagong', 'Hamilton', 'Paarl',
       'Barbados', 'Cardiff', 'Manchester', 'Perth', 'Taunton',
       'Lauderhill', 'Gros Islet', 'Nagpur', 'Basseterre', 'Mumbai',
       'Chattogram', 'Sharjah', 'Kandy', 'Karachi', 'East London',
       'Potchefstroom', 'Nottingham', 'Dharmasala', 'Dhaka', 'Centurion',
       'Jamaica', 'Victoria', 'Indore', 'Southampton', 'Hobart',
       'Dehradun', 'Brisbane', 'Hyderabad', 'Providence', 'St Vincent',
       'Bangalore', 'King City', 'Bengaluru', 'Antigua', 'Dharamsala',
       'Carrara', 'Sylhet', 'Bloemfontein', 'Nairobi']
st.title('Score Predictor')
col, col1, col2 = st.columns(3)
with col:
    Format=st.selectbox('Format',sorted(['t-20', 'ODI']))
with col1:
    batting_team = st.selectbox('Batting Team', sorted(teams))
with col2:
    bowling_team = st.selectbox('Bowling Team', sorted(teams))
city = st.selectbox('City', sorted(citys))
col3,col4,col5 = st.columns(3)
with col3:
    current_score = st.number_input('Current Score')
with col4:
    if Format == 't-20':
        over = st.number_input('Overs done(works for over >5)')
    else :
        over = st.number_input('Overs done(works for over >10)')
with col5:
    wicket=st.number_input('Wickets out')
if Format == 't-20':
    last_five=st.number_input('Run scored in last 5 overs')
else:
    last_10_over = st.number_input('Run scored in last 10 overs')
if st.button('Predict Score'):
    if Format == 't-20':
        ball_left = 120-(6*over)
    else:
        ball_left = 300-(6*over)
    crr = current_score/over
    wicket_left = 10-wicket
    if Format == 't-20':
        input_df=pd.DataFrame({
            'batting_team': [batting_team],
            'bowling_team': [bowling_team],
            'city': [city],
            'current_score': [current_score],
            'balls_left': [ball_left],
            'wicket_left': [wicket_left],
            'crr': [crr],
            'last_five': [last_five]
        })
        result = pipe_t20.predict(input_df)
    else:
        input_df = pd.DataFrame({
            'batting_team': [batting_team],
            'bowling_team': [bowling_team],
            'city': [city],
            'score': [current_score],
            'ball_left': [ball_left],
            'wicket_left': [wicket_left],
            'crr': [crr],
            'last_10_over': [last_10_over]
        })
        result = pipe_odi.predict(input_df)
    st.title(int(result))