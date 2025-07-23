import ollama

model_name = "llama3.2"

prompt = input("prompt: ")

# response = ollama.generate(model=model_name, prompt=prompt)

response = ollama.chat(model=model_name, messages = [{'role': 'user', 'content': prompt}])
print(response)

print(type(response))
# print(response.response)
print(response['message']['content'])