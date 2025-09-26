from configparser import ConfigParser

class Config():

    def __init__(self, config_file = "./src/LangGraphAgenticAI/ui/uiconfigfile.ini"):
        self.config = ConfigParser()
        self.config.read(config_file)

    def get_llms(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ")
    
    def get_usecases(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(", ")
    
    def get_model_options(self):
        return self.config["DEFAULT"].get("GEMINI_MODEL_OPTIONS").split(", ")
    
    def get_page_title(self):
        print("This page Title being called")
        print(self.config)
        # print(self.config["DEFAULT"].get("PAGE_TITLE"))
        return self.config["DEFAULT"].get("PAGE_TITLE")


# llms = Config()
# result = llms.get_page_title()
# print(result)