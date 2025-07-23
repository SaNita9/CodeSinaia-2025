import ollama

class SmartAgent:

    def __init__(self, model_name):
        # print("Agent created")
        self.model_name = model_name

    def chat(self, chat_log):
        answer = ollama.chat(
            model = self.model_name, 
            messages = chat_log)
        return answer