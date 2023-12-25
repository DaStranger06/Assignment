import streamlit as st
from PIL import Image
from utility import login
from src.conn import get_database_connection


logo_image = Image.open("img/logo.png")
banner_img = Image.open("img/banner.png")


st.set_page_config(page_title="Welcome", page_icon=logo_image, layout="wide")

col1, col2 = st.columns([1, 3])

with col1:
    st.image(logo_image, width=100)

with col2:
    st.markdown("# Welcome to the Page")

def menu():
    st.sidebar.header('Select')
    task = st.sidebar.selectbox('-----', ('Save', 'Insert', 'Report'))

    if task == 'Save ':
        cursor, db = get_database_connection()
     
    elif task == 'Reporting':
        pass
     
    elif task == 'Parameter Insertion':
        pass

@login
def main():
    col1, col2, col3 = st.columns((1, 4, 1))
    col2.markdown("<h1 style='text-align: left;margin-top:-2rem; margin-left:1rem; color: #E12D06;'>Expense Tracker</h1>",
                  unsafe_allow_html=True)
    st.write('\n')

    if st.session_state["authentication_status"]:
        menu()

if __name__ == '__main__':
    main()