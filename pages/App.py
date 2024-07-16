import streamlit as st
import streamlit_authenticator as stauth
import toml
from streamlit_authenticator.utilities.exceptions import LoginError

st.set_page_config(
    page_title="App",
    page_icon=":material/favorite:",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={
        'Get Help': 'mailto:mohit.patil@cogentinfo.com',
        'Report a bug': "mailto:mohit.patil@cogentinfo.com",
        'About': "# © Cogent Infotech"
    }
)

# Loading config file
with open('.streamlit/secrets.toml', 'r', encoding='utf-8') as file:
    config = toml.load(file)

# Creating the authenticator object
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['pre-authorized']
)

# Creating a login widget
try:
    authenticator.login(location='sidebar',
                        fields={
                            'Form name': 'Login to Cogentinfo AI',
                            'Username': 'Username',
                            'Password': 'Password',
                            'Login': 'Login',
                        }
                        )
except LoginError as e:
    st.error(e)

with st.sidebar:
    if st.session_state["authentication_status"]:
        authenticator.logout()
        st.write(f'Welcome *{st.session_state["name"]}*')
    elif st.session_state["authentication_status"] is False:
        st.error('Username/password is incorrect')
    elif st.session_state["authentication_status"] is None:
        st.warning('Please enter your username and password')

# # Saving config file
# with open('.streamlit/secrets.toml', 'w', encoding='utf-8') as file:
#     toml.dump(config, file)

if st.session_state["authentication_status"] is False:
    st.warning("Please Login first", "🚨",)

if st.session_state["authentication_status"]:
    st.title("Main App")

    st.write("This is a sample web app for Cogentinfo AI.")
