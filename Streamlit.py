#!/usr/bin/env python
# coding: utf-8



import streamlit as st
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import pickle
from PIL import Image
import requests
import time





# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)




df = pd.read_csv('file1.csv', index_col=0)


with open('finalpipe1.pkl' , 'rb') as f:
    lr = pickle.load(f)



# Add title
st.title("MVP Prediction Stats :trophy:")
st.image("Images/lebron-james-.jpeg", use_column_width= 'always')

# Add subtitle
st.markdown("Enter the following statistics for any player and receive a MVP prediction!")



# Add sidebar
st.sidebar.markdown("## Predict what it will take for your favorite player to win NBA MVP")
st.sidebar.image("Images/946185_nba-mvp-meta.png", width = 200)
st.sidebar.caption("About This App:")
st.sidebar.caption("Using a machine learning model, this application allows users to provide their own inputs and 2022 season data to predict this years MVP.")

# Sidebar cont.
st.sidebar.markdown("#### Built by Troy Hendrickson")
st.sidebar.caption("Github: https://github.com/tkhendrix22/NBA-MVP-Prediction")
st.sidebar.caption("LinkedIn: https://www.linkedin.com/in/troy-hendrickson/")


st.write("---")
names = st.selectbox('Select Player:',
                     df['player_name'].unique())
'You selected: ', names

st.write("---")
team = st.selectbox('Select team:',
                    df['team'].unique())
'You selected: ', team
if st.button('see player stats'):
    st.write(df[(df['player_name'] == names) & (df['team'] == team)][['pts','ast','reb','total_games','win_pct']])




st.write('---')
points = st.slider('pts', 0, 40, 1)
st.write(points, 'Points Per Game')
'You selected: ', points

st.write("---")
asts = st.slider('ast', 0, 15, 1)
st.write(asts, 'Ast Per Game')
'You selected: ', asts

st.write("---")
rebs = st.slider('reb',0, 20, 1)
st.write(rebs, 'Rebs Per Game')
'You selected: ', rebs

st.write("---")
games = st.slider('total_games',0, 82, 1 )
st.write(games, 'Total Games Played')
'You selected: ', games

st.write("---")
wp = st.slider('win_pct',1,100,1) /100
st.write(wp, 'Win Percentage')
'You selected: ', wp

st.write("---")
newteam = st.selectbox('Select  new team:',
                    df['team'].unique())


if st.button('Predict'):
    
    #Unpickle the model
    with open('finalpipe1.pkl' , 'rb') as f:
        lr = pickle.load(f)
        
    vec = df[(df['player_name'] == names) & (df['team'] == team)]
    vec['pts'] = points
    vec['ast'] = asts
    vec['reb'] = rebs
    vec['total_games'] = games
    vec['win_pct'] = wp
    vec['team'] = newteam
    st.write(vec)
    
    
    # get prediction
    prediction = lr.predict(vec)
    
    if prediction[0] == 0 :
            st.error('Will not win MVP :thumbsdown:')
            
    elif prediction[0] == 1 :
            st.success('Congratulations to your new 2023 NBA MVP! :thumbsup:')  
            
    with st.spinner('Calculating...'):
        time.sleep(1)
    #st.success('Done!')
    
    st.write(prediction)
    
    


       

# Add vectors of stats
vec = df[(df['player_name'] == names) & (df['team'] == team)]
vec['pts'] = points
vec['ast'] = asts
vec['reb'] = rebs
vec['total_games'] = games
vec['win_pct'] = wp





st.write("---")
st.header('Get In Touch With Me!')
st.write('##')
    
contact_form = """
<form action="https://formsubmit.co/troykhendrickson@gmail.com" method="POST">
     <input type='hidden' name='_captcha' value='false'>
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
"""




left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()







