import streamlit as st
import streamlit_authenticator as stauth
# import pyyaml module
import yaml
from yaml.loader import SafeLoader


with open('users/config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)


authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

### print repeat two time whenever you refresh the page ---> check why!!! ###
# print('suck my dik')

# print(config['preauthorized'])


## preauthorization True so only people with the email in config.yaml 'preauthorized' can register 
## after they signed up their email will be removed from the yaml file
try:
    if authenticator.register_user('Register user', preauthorization=True):
        st.success('User registered successfully')
except Exception as e:
    st.error(e)

with open('users/config.yaml', 'w') as file:
    yaml.dump(config, file, default_flow_style=False)