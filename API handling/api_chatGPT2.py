import openai
import os


prompt = input("What to ask Davinci? > ")
openai.api_key = os.getenv('YOUR_API_KEY')

response = openai.Completion.create(model="text-davinci-003", prompt=prompt)

print(response)


