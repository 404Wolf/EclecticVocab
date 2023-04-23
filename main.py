from dotenv import load_dotenv
from os import getenv
import openai
import json
load_dotenv()

input_word = input("Enter a word: ")

openai.api_key = getenv("TOKEN")
with open("system.txt") as systemFile:
    system_description = systemFile.read()

output = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": system_description},
        {"role": "user", "content": input_word},
    ],
)["choices"][0]["message"]["content"]

try:
    output = json.loads(output)
except json.decoder.JSONDecodeError:
    print("Error: Output is not valid JSON")
    print(output)

with open(f"outputs/{output['word'].lower()}.json", "w") as outputFile:
    json.dump(output, outputFile, indent=4)
