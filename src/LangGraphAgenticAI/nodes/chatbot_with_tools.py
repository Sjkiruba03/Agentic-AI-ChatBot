from src.LangGraphAgenticAI.state.state import State


class ChatBotwithTools():

    """
    Creating an chatbot with tool funtionality
    """

    def __init__(self,llm):
        self.model = llm

    def process(self, state:State):
        """
        this funtion will process the input and return the response with Tools inegration
        """
        user_input = state['messages'][-1] if state['messages'] else ""
        llm_response = self.model.invoke([{"role": "user", "content": user_input}])

        ## Simultae the tool specifuc logic
        tools_response = f"Tools integration for: {user_input}"
        return {"messages": [llm_response, tools_response]}
    
    def create_chatbot(self, tool):
        """
        Return a chatbot node funtion
        """
        llm_with_tools = self.model.bind_tools(tool)
        print("binded")

        def chatbot_node(state:State):
            """
            creating an logic for processing the input and retuning an response
            """
            print("second method called")
            return {"messages": [llm_with_tools.invoke(state['messages'])]}
        
        print("stuckeds")
        
        
        return chatbot_node