import os
from contextlib import suppress

from dotenv import load_dotenv
from os import getenv
import openai
import json

from vocab.vocab import Vocab

load_dotenv()


def main():
    input_word = input("Enter a word: ")

    openai_api_key = getenv("TOKEN")
    with open("vocab/system.txt") as systemFile:
        system_description = systemFile.read()

    vocab = Vocab(system_description, openai_api_key)
    output = vocab.fetch_word(input_word).asDict()
    word = output['word'].lower()

    with suppress(FileExistsError):
        os.mkdir(f"outputs/{word}")
    vocab.fetch_image(input_word, f"outputs/{word}/image.png")
    vocab.fetch_audio(input_word, f"outputs/{word}/audio.mp3")
    with open(f"outputs/{word}/data.json", "w") as outputFile:
        json.dump(output, outputFile, indent=4)


if __name__ == "__main__":
    main()
