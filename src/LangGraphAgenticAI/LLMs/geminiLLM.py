import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
from src.LangGraphAgenticAI.ui.streamlitui.load_ui import LoadStreamlitUI

from langchain.chat_models import init_chat_model

# os.environ["GEMINI_API_KEY"]=os.getenv("GEMINI_API_KEY")
# os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
# os.environ["HUGGING_API_KEY"]=os.getenv("HUGGING_API_KEY")

api = 'AIzaSyAVhPRqdE_7L08sc-ispUeis7y8OoE0tU4'
TAVILY_API_KEY='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'


API_KEY = os.getenv('GEMINI_API_KEY')

class GeminiLLm():
    def __init__(self, user_control_input):
        self.user_control_input = user_control_input

    def load_llm(self):
        try:
            gemini_model = self.user_control_input['selected_gemini_model']
            api = self.user_control_input['GEMINI_API_KEY']
            if api == '' and os.getenv['GEMINI_API_KEY'] == '':
                st.error("Please provide the API key")

            # os.environ['GEMINI_API_KEY'] = os.getenv('GEMINI_API_KEY')

            # Initialize my LLM model
            model = init_chat_model(model=gemini_model, model_provider="google_genai",api_key = api)

        except Exception as e:
            raise ValueError(f"Got an error in API key: {e}")
        return model







        

        