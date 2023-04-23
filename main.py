from pprint import pprint

from dotenv import load_dotenv
from os import getenv
import openai
import json
load_dotenv()

openai.api_key = getenv("TOKEN")
with open("system.txt") as systemFile:
    system_description = systemFile.read()

output = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": system_description},
        {"role": "user", "content": "careen"},
    ],
)

print(output)
output = output["choices"][0]["message"]["content"]
with open("output.json", "w") as outputFile:
    json.dump(json.loads(output), outputFile, indent=4)
