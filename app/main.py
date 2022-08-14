import streamlit as st
import pandas as pd
import sys
# adding helper_functions folder to the system path
## this way we can import the package /python script inside of it

#sys.path.insert(0, '../helper_functions') ## might create problems. ORGANIZE BETTER THE STRUCTURE OF FILES!
from packages.Anima_creation import Animal

st.set_page_config(layout="wide")
st.image('images/iron-throne.jpg')

### create containers to separate information
header = st.container()
graf_container = st.container()

### create a form stramlit object 
form_1 = st.form('myform')



with header:
    ### title 
    #st.title('Our Space <3')

    ## we can write text with markdown and allow it to read html and css code to style the page 
    st.markdown("<h1 style='text-align: center; color: plum;'>Our Space <3 🦊🥺</h1>", unsafe_allow_html=True)


    st.markdown("""<h3 style='text-align: center; color: grey;'>
    Hello We are Gladys & José, Not Nice to meet you!</h3>
    """, unsafe_allow_html=True)


    st.write("""This is the begining
    of all the cool things!
    """)

    ### create columns 
    col1, col2, col3, col4 = st.columns(4)

    ## make an api call for this 
    ## or for lab percentage (above average of the week.... something of the sort)

    col1.metric(label="Completed", value=10, delta=2)
    col4.metric(label="Temperature", value="70 °F", delta="1.2 °F") 
    col2.metric(label="To Finish", value=30, delta=-2)
    col3.metric(label="Optional done", value=1, delta=1)
    
    ## not ordered on purpose
    ## the orderd is associated to the moment of creation as well as the position (st.columns(4)) above

with graf_container:

    ## playing around
    ## for better charts might be needed to install 'plotly' module
    data = pd.read_csv('data/team_heart.csv')
    st.area_chart(data=data['Age'])



with form_1:
    ## Text input
    name = st.text_input("What is your name")
    ### let's see if we can retrive some values from picks done by the ###
    ### users in streamlit objects ###
    date = st.date_input("When were you born")
    ### we can retrive data from streamlit ###

    type_ani = st.radio("What's animal", ('Dog', 'Cat', 'Other'))
    name_ani = st.text_input("What's animal name")
    age_ani = st.number_input("What's animal Age")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")

    if submitted == True:
        animal = Animal(type_ani, name_ani,age_ani, name)
        animal_df = animal.fram_creation()
        animal_df.to_csv('data/animal_info.csv', index=False)

if submitted:
    #st.write(animal_df) ## write can also write tables  == st.dataframe(animal_df)
    st.table(animal_df) ## static tables