import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
from src.LangGraphAgenticAI.ui.streamlitui.load_ui import LoadStreamlitUI
from src.LangGraphAgenticAI.LLMs.geminiLLM import GeminiLLm
from src.LangGraphAgenticAI.graph.graph_builder import GraphBuilder
from src.LangGraphAgenticAI.ui.streamlitui.display_result import DisplayResultsInStreamlit


def load_langgrapg_agentic_app():

    """
     Load and run the LangGraph Agentic AI Application with Streamlit
     This funtion intialize the UI Part and Get the user input , configure the LLM model
     Set the Graph based on the user selected UseCase and display the Output 

    """

    # Load UI
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Failed to Load User inout from UI")
        return
    
    ## text input for user message
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe
    else:
        user_message = st.chat_input("Enter Your Message..!")

    if user_message:

        try:
            ## Integrate the LLM to start
            llm_config = GeminiLLm(user_control_input=user_input)
            model = llm_config.load_llm()

            if not model:
                st.error("The LLM model is not intialized yet")
                return

            use_case = user_input.get('Selected_usecase')
            if not use_case:
                st.error("Please Select the Use case to proceed")
                return
            
            ## Graph Builder
            graph_builder = GraphBuilder(model)

            try:
                print("hi enter into try block")
                graph = graph_builder.setup_graph(use_case)
                print("graph has been intialized")
                print(user_message)
                DisplayResultsInStreamlit(use_case, graph, user_message).display_result()

            except Exception as e:
                st.error("Graph setup is failed")
                return

        
        except Exception as e:
            st.error(f"The user messages part is failed : {e}")
            return
    



