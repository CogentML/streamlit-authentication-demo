import streamlit as st
import streamlit_authenticator as stauth
import toml
from streamlit_authenticator.utilities.exceptions import LoginError

st.set_page_config(
    page_title="Home",
    page_icon=":material/home:",
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

# Saving config file
with open('.streamlit/secrets.toml', 'w', encoding='utf-8') as file:
    toml.dump(config, file)

# Title Element
st.markdown(
    body="""<h1 style='text-align: center; color: #A94438;'>
            App Title
            </h1>""",
    unsafe_allow_html=True
)
# Set the app description
st.markdown(
    body="""<h3 style='text-align: center; color: black;'>
            About
            </h3>""",
    unsafe_allow_html=True
)
# Set the app description
st.caption(
    """
        App Description
    """
)
# add a horizontal line
st.divider()

# Define navigation elements using columns
col1, col2, col3 = st.columns(spec=[0.3, 0.4, 0.3], gap='medium')

# Empty column for spacing in the left
with col1:
    pass

# Button to navigate to the next page
with col2:
    if st.button(
        label="Lets begin :point_right:",
        help="Click here to try out our solution :magic_wand:",
        type="primary",
        use_container_width=True,
    ):
        if st.session_state["authentication_status"]:
            st.switch_page("pages/App.py")
        elif st.session_state["authentication_status"] is False:
            st.error('Username/password is incorrect')
        elif st.session_state["authentication_status"] is None:
            st.warning('Please enter your username and password')

# Empty column for spacing in the right
with col3:
    pass
