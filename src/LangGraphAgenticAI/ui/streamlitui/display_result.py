import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage, ToolMessage
import json

class DisplayResultsInStreamlit:

    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result(self):
        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message
        if usecase == "Basic ChatBot":
            print("use case has selected")
            for event in graph.stream({"messages":("user", user_message)}):
                print("for loop is running")
                print(event.values())
                for value in event.values():
                    print(value['messages'])
                    with st.chat_message("user"):
                        st.write(user_message)
                    with st.chat_message("Assistent"):
                        st.write(value['messages'].content)
        elif usecase == "ChatBot with Tools":
            ## prepare state and invoke graph
            initial_message = {"messages": [user_message]}
            print("message invoked")
            res = graph.invoke(initial_message)
            for message in res['messages']:
                if type(message) == HumanMessage:
                    with st.chat_message("User"):
                        st.write(message.content)
                elif type(message) == ToolMessage:
                    with st.chat_message("Assistent"):
                        st.write("Tool call Start")
                        st.write(message.content)
                        st.write("Tool call End")
                elif type(message) == AIMessage and message.content:
                    with st.chat_message("Assistant"):
                        st.write(message.content)
        elif usecase == "AI News":
            frequency = self.user_message
            with st.spinner(" Fetching and summarizing the News..."):
                result = graph.invoke({'messages': frequency})
                try:
                    ## Read the Markdown file
                    AI_NEWS_PATH = f"./AINews/{frequency.lower()}_summary.md"
                    with open(AI_NEWS_PATH, "r") as f:
                        markdown_content = f.read()


                    ## Display the markdown content in streamlit
                    st.markdown(markdown_content, unsafe_allow_html=True)
                except FileNotFoundError:
                    st.error(f"File not generated or File not found: {AI_NEWS_PATH}")
                except Exception as e:
                    st.error(f"An error occured : {str(e)}")
                    


        