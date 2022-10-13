import streamlit as st

def app():
    st.header("select session to Delete")
    option = st.selectbox(
        'Sessions :',
        ('6666 ', 'classroom 5', '1648'))
    if st.button('Delete Session'):
        if option == "6666":
            st.write('Deleted')