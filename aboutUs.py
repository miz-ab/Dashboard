import streamlit as st

st.title(" Swahili-Speech-To-Text ")
st.write("""
# About Group 5

## Team members
""")
col1, col2, col3 = st.columns(3)
with col1:
    st.header("Zelalem")
    st.image("https://static.streamlit.io/examples/cat.jpg")

    st.text_area('Zelalem', '''
    ...     It was the best of times, it was the worst of times, it was
    ...     the age of wisdom, it was the age of foolishness, it was
    ...     the epoch of belief, it was the epoch of incredulity, it
    ...     was the season of Light, it was the season of Darkness, it
    ...     was the spring of hope, it was the winter of despair, (...)
    ...     ''')

with col2:
    st.header("Abubakar")
    st.image("https://static.streamlit.io/examples/cat.jpg")

    st.text_area('Abubakar', '''
    ...     It was the best of times, it was the worst of times, it was
    ...     the age of wisdom, it was the age of foolishness, it was
    ...     the epoch of belief, it was the epoch of incredulity, it
    ...     was the season of Light, it was the season of Darkness, it
    ...     was the spring of hope, it was the winter of despair, (...)
    ...     ''')

with col3:
    st.header("Binyam Sisay")
    st.image("https://static.streamlit.io/examples/cat.jpg")

    st.text_area('Binyam Sisay', '''
    ...     It was the best of times, it was the worst of times, it was
    ...     the age of wisdom, it was the age of foolishness, it was
    ...     the epoch of belief, it was the epoch of incredulity, it
    ...     was the season of Light, it was the season of Darkness, it
    ...     was the spring of hope, it was the winter of despair, (...)
    ...     ''')

col4, col5, col6 = st.columns(3)
with col4:
    st.header("col4")
    st.image("https://static.streamlit.io/examples/cat.jpg")

    st.text_area('col4', '''
    ...     It was the best of times, it was the worst of times, it was
    ...     the age of wisdom, it was the age of foolishness, it was
    ...     the epoch of belief, it was the epoch of incredulity, it
    ...     was the season of Light, it was the season of Darkness, it
    ...     was the spring of hope, it was the winter of despair, (...)
    ...     ''')

with col5:
    st.header("col5")
    st.image("https://static.streamlit.io/examples/cat.jpg")

    st.text_area('col5', '''
    ...     It was the best of times, it was the worst of times, it was
    ...     the age of wisdom, it was the age of foolishness, it was
    ...     the epoch of belief, it was the epoch of incredulity, it
    ...     was the season of Light, it was the season of Darkness, it
    ...     was the spring of hope, it was the winter of despair, (...)
    ...     ''')

with col6:
    st.header("col6")
    st.image("https://static.streamlit.io/examples/cat.jpg")

    st.text_area('col6', '''
    ...     It was the best of times, it was the worst of times, it was
    ...     the age of wisdom, it was the age of foolishness, it was
    ...     the epoch of belief, it was the epoch of incredulity, it
    ...     was the season of Light, it was the season of Darkness, it
    ...     was the spring of hope, it was the winter of despair, (...)
    ...     ''')
