import streamlit as st
import time

from src.main import simulate_mh_problem


st.title('Monty Hall Problem Simulator')

num_of_games = st.number_input('Enter number of games to simulate', min_value=1, max_value=100000, value=100)

col1, col2 = st.columns(2)

col1.subheader('Win Percentage with switching doors:')
col2.subheader('Win Percentage without switching doors:')

chart1= col1.line_chart(x=None, y=None, width=0, height=400)
chart2= col2.line_chart(x=None, y=None, width=0, height=400)



wins_with_switch = 0
wins_without_switch = 0

for i in range(num_of_games):
    num_of_wins_without_switch, num_of_wins_with_switch = simulate_mh_problem(num_of_games)
    
    wins_with_switch += num_of_wins_with_switch
    wins_without_switch += num_of_wins_without_switch 
    
    chart1.add_rows([wins_with_switch / (i + 1)])
    chart2.add_rows([wins_without_switch / (i + 1)])
    
    time.sleep(0.001)

st.success(f'Win Percentage with switching doors: {wins_with_switch / (wins_with_switch + wins_without_switch) * 100}%')
st.success(f'Win Percentage without switching doors: {wins_without_switch / (wins_with_switch + wins_without_switch) * 100}%')
