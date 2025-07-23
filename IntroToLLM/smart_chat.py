from smart_agent import SmartAgent

smart_agent = SmartAgent("llama3.2")

chat_log = []
question = input("Question: ").strip()
while question != "/pa":
    if question != "":
        # print(f"Question is {question}")
        chat_log.append({'role': 'user', 'content': question})
        # response = ollama.chat(
        #     model=model_name, 
        #     messages = chat_log)
        answer = smart_agent.chat(chat_log)
        answer_text = answer['message']['content']
        chat_log.append({'role': 'agent', 'content': answer_text})
        print(answer_text)
    question = input("Question: ").strip()