from langgraph.graph import StateGraph, END, START
from src.LangGraphAgenticAI.state.state import State

from src.LangGraphAgenticAI.nodes.basic_chatbot_node import BasicChatbotNode
from src.LangGraphAgenticAI.tools.search_tool import get_tools,create_tool_node
from langgraph.prebuilt import ToolNode, tools_condition
from src.LangGraphAgenticAI.nodes.chatbot_with_tools import ChatBotwithTools
from src.LangGraphAgenticAI.nodes.ai_news_node import AINews


class GraphBuilder():

    def __init__(self, llm):

        self.model = llm
        self.graph_builder = StateGraph(State)

    def built_basic_chatbot_graph(self):
        """
        Build an basic chatbot in langgraph
        This method will intialize the chatbot node 
        and inegerate into the graph . The chatbot node is set at both end of graph
        """
        self.chatbot = BasicChatbotNode(self.model)

        self.graph_builder.add_node("chatbot",self.chatbot.process)

        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)

    def chatbot_with_tools(self):
        """
        Builds an advanced chatbot graph with tool integration
        This method create a chatbot graph that include both chatbot node 
        and a tool node. It defines tool, initialize the chatbot with tool 
        capabilities , and sets up the conditional and direct edge between the nodes.
        Tht chatbot node will set as an entry Point
        """
       
        tools = get_tools()
        
        tool_node = create_tool_node(tools)

        llm = self.model
        chatbot_tools = ChatBotwithTools(llm)
        chat_bot = chatbot_tools.create_chatbot(tools)
        ## Add nodes
        self.graph_builder.add_node("chatbot", chat_bot)
        self.graph_builder.add_node("tools", tool_node)


        ## Add edges
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges("chatbot", tools_condition)
        self.graph_builder.add_edge("tools", "chatbot")

        print("finised the graph")

    def fetch_ai_news(self):

        """
        Creating an with function with tool integeration and summarize and save in files
        """
        print("entered fetch_ai_news")
        llm = self.model
        ainews = AINews(llm)
        fetch_news = ainews.fetch_news
        summarizer = ainews.summarize_news
        save_file = ainews.save_file
        print("called")
        self.graph_builder.add_node("fetch_news",fetch_news)
        self.graph_builder.add_node("summarizer",summarizer)
        self.graph_builder.add_node("save_file",save_file)

        ## Add edges
        print("node added")
        self.graph_builder.add_edge(START, "fetch_news")
        self.graph_builder.add_edge("fetch_news", "summarizer")
        self.graph_builder.add_edge("summarizer","save_file")
        self.graph_builder.add_edge("save_file", END)

        print("Graph finished")
        

    def setup_graph(self, usecase:str):
        """
        Set up the graph for selected Use Case
        """
        if usecase == "Basic ChatBot":
            self.built_basic_chatbot_graph()
        elif usecase == "ChatBot with Tools":
            print("entered the chatbot with tool case")
            self.chatbot_with_tools()
            print("chat bot tool called")
        elif usecase == "AI News":
            print("entered into graph caller part")
            self.fetch_ai_news()

            
        return self.graph_builder.compile()