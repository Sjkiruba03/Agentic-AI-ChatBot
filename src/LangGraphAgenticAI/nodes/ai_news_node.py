from tavily import TavilyClient
from langchain.prompts import ChatPromptTemplate


class AINews():
    def __init__(self, llm):
        
        """
        Initialize the tavilynews node  key API 
        """
        self.tavily = TavilyClient()
        self.llm = llm
        ## This is used to capture various steps in this file so later can be used for steps down
        self.state = {}

    def fetch_news(self, state: dict):
        """
        Fetch AI news based on the specified frequency.
        Args:
            state(dict): The State dictionary containing 'frequency'.
        Returns:
            dict : Updated date with 'news_data' key containing fetched news.
        """

        frequency = state['messages'][0].content.lower()
        self.state['frequency'] = frequency
        time_range_map = {'daily':'d', 'monthly':'m', 'weekly': 'w', 'yearly': 'y'}
        days_map = {'daily':1, 'weekly': 7 , 'monthly': 30, 'yearly': 366}

        response = self.tavily.search(
            query= "Top Artificial intelligence (AI) technology news in india and Globally",
            topic="news",
            time_range=time_range_map[frequency],
            include_answer="advanced",
            max_results="20",
            days=days_map[frequency]
        )

        state['news_data'] = response.get('results',[])
        self.state['news_data'] = state['news_data']
        print("fetched")
        return state
    
    def summarize_news(self, state: dict):
        """
        Summarize the fetched News using the LLM

        Args:
            state(dict) : The state dictionary containing "new_data"

        Returns:
            dict : Updated State with 'summary' key containing the summarized news         
        """
        print("entered into smmarixer")
        news_items = self.state['news_data']
        prompt_template = ChatPromptTemplate.from_messages([
            ("system", """
                        Summarize the AI news article into markdown format . For each item include,
                        - Date in **YYYY-MM-DD** format in IST timezone
                        - concise the sentence summary from latest news
                        - Sort news by date wise( Latest news)
                        - Source URL as link

                        ### [date]
                        - [Summary] (URL)  
                        """),
            ("user", "Help me to summarize this: \n{articles}")
            ])
        
        article_str = "\n\n".join([
            f"Content: {item.get('content','')}\nURL: {item.get('content','')}\nDate: {item.get('content','')}"
            for item in news_items
        ])
        print("going to call llm")
        response = self.llm.invoke(prompt_template.format(articles=article_str))
        print(response.content)
        print("getting the response from LLm")
        state['summary'] = response.content
        self.state['summary'] = state['summary']
        print("summerized")
        return self.state
        
    def save_file(self, state):
        print("save_file entered")
        frequency = self.state['frequency']
        summary = self.state['summary']
        filename = f"./AINews/{frequency}_summary.md"
        print("going to open")
        with open(filename, 'w') as f:
            print("opened the file properly")
            f.write(f" # {frequency.capitalize()} AI News Summary \n\n")
            print("problem is here")
            f.write(summary)
            print("writed")
        print("file writed into the location")
        self.state['filename'] = filename
        print("saved into file")
        return self.state

