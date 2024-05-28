import streamlit as st


def app():
    # st.title()
    import streamlit as st

    original_title = '<h1 style= color:black; font-size: 20px;text-align: center;">✨통합 FAQ 조회 시스템✨ </h1>'
    # st.markdown("<h1 style='text-align: center;'>ABOUT</h1>", unsafe_allow_html=True)

    st.markdown(original_title, unsafe_allow_html=True)


    # Set the background image
    background_image = """
    <style>
    [data-testid="stAppViewContainer"] > .main {
        background-image: url("https://file3.instiz.net/data/file3/2019/08/17/6/6/f/66f712184d5cfd4b9b6593299d934a7c.gif");
        background-size: cover;
    }
    </style>
    """

    st.markdown(background_image, unsafe_allow_html=True)

    # st.text_input("", placeholder="Streamlit CSS ")

    input_style = """
    <style>
    input[type="text"] {
        background-color: transparent;
        color: #a19eae;  // This changes the text color inside the input box
    }
    div[data-baseweb="base-input"] {
        background-color: transparent !important;
    }
    [data-testid="stAppViewContainer"] {
        background-color: transparent !important;
    }
    </style>
    """
    st.markdown(input_style, unsafe_allow_html=True)
   

    

      


