import streamlit as st
import os

from src.LangGraphAgenticAI.ui.uiconfigfile import Config


class LoadStreamlitUI():

    def __init__(self):
        self.config = Config()
        self.user_control = {}

    def load_streamlit_ui(self):
        st.set_page_config(page_title= self.config.get_page_title(), layout="wide")
        st.header(self.config.get_page_title())
        st.session_state.timeframe = ''
        st.session_state.IsFetchButtonClicked = False

        with st.sidebar:
            ## Get LLM options from config
            llm_options = self.config.get_llms()
            usecase_options = self.config.get_usecases()


            ## LLM Selections
            self.user_control['Selected_LLM'] = st.selectbox("Select LLM", llm_options)

            if self.user_control['Selected_LLM'] == 'Gemini':
                
                model_options = self.config.get_model_options()
                self.user_control['selected_gemini_model'] = st.selectbox("SelectModel",model_options)
                self.user_control['GEMINI_API_KEY'] = st.session_state['GEMINI_API_KEY'] = st.text_input("API Key",type="password")
                ## We will get warning if user doesnt provide any API key

                if not self.user_control['GEMINI_API_KEY']:
                    st.warning("Please Provide the gemini API key to proceed further, If you don't have Please Refer : https://aistudio.google.com")

            ## Use case selection Select 
            self.user_control['Selected_usecase'] = st.selectbox("Select UseCase", usecase_options)

            if self.user_control['Selected_usecase'] == 'ChatBot with Tools':
                os.environ['TAVILY_API_KEY']=self.user_control['TAVILY_API_KEY'] = st.session_state['TAVILY_API_KEY'] = st.text_input("API_KEY", type="password")

                if not self.user_control['TAVILY_API_KEY']:
                    st.warning("Please provide the tavily API to access tools , if you don't have Please refer : https://app.tavily.com/home")


            if self.user_control['Selected_usecase'] == "AI News":
                
                os.environ['TAVILY_API_KEY']=self.user_control['TAVILY_API_KEY'] = st.session_state['TAVILY_API_KEY'] = st.text_input("API_KEY", type="password")
                if not self.user_control['TAVILY_API_KEY']:
                    st.warning("Please provide the tavily API to access tools , if you don't have Please refer : https://app.tavily.com/home")

                st.subheader(" AI News Explorer")
                with st.sidebar:
                    time_frame = st.selectbox("Select Time Frame",
                                                  ["Daily", "Weekly","Monthly"],
                                                  index=0
                                                  )
                if st.button(" Fetch Latest AI News", use_container_width=True):
                    st.session_state.IsFetchButtonClicked = True
                    st.session_state.timeframe = time_frame

                


        return self.user_control