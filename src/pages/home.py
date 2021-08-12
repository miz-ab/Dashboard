
import streamlit as st
import awesome_streamlit as ast


def write():
   
    with st.spinner("Loading Home ..."):
        st.title('Speech To Text Transcription for Swahili')

        st.header("About Swahili")
        col1, mid, col2 = st.columns([30,2,30])
        with col1:
            st.image('images/Lang.jfif')
        with col2:
                st.write("""
                The language that is primarily spoken by Swahili is called KiSwahili or Bantu. This language has origins from the Arabic language but is considered Bantu because of the suffixes and roots of the language. only five million people speak this language as their first language but around 140 million people use the language to communicate.
                """)
        st.header("Overview")
        st.subheader("Business Need")
        st.write(
            """
           Speech recognition technology allows for hands-free control of smartphones, speakers,
           and even vehicles in a wide variety of languages. Companies have moved towards the
           goal of enabling machines to understand and respond to more and more of our
           verbalized commands. There are many matured speech recognition systems available,
           such as Google Assistant, Amazon Alexa, and Apple’s Siri. However, all of those voice
           assistants work for limited languages only.
                """
        )
        st.write(
            """
            The World Food Program wants to deploy an intelligent form that collects nutritional information of food bought and sold at markets in two different countries in Africa - Ethiopia and Kenya. The design of this intelligent form requires selected people to install an app on their mobile phone, and whenever they buy food, they use their voice to activate the app to register the list of items they just bought in their own language. The intelligent systems in the app are expected to live to transcribe the speech-to-text and organize the information in an easy-to-process way in a database. 
            """
        )
