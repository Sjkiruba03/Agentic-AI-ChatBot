from src.LangGraphAgenticAI.state.state import State


class BasicChatbotNode():

    """
    Creating an basic Chatbot node
    """

    def __init__(self,llm):
        self.model = llm

    def process(self, state:State):
        """
        this funtion will process the input and return the response
        """
        return {"messages": self.model.invoke(state['messages'])}