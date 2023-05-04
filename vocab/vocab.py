import json
from dataclasses import InitVar, dataclass, asdict
import base64

from dotenv import load_dotenv
import openai
from gtts import gTTS

load_dotenv()


@dataclass(slots=True)
class Word:
    word: str
    openai_api_key: str
    system_description: str
    fetch_on_init: InitVar[bool] = True

    part_of_speech: str = None
    pronunciation: str = None
    definitions: list[str] = None
    synonyms: list[str] = None
    examples: list[str] = None

    WORD_ATTRS = (
        "word",
        "part_of_speech",
        "pronunciation",
        "definitions",
        "synonyms",
        "examples",
    )

    def __post_init__(self, fetch_on_init: bool) -> None:
        if fetch_on_init:
            self.fetch()

    def fetch(self) -> None:
        output = openai.ChatCompletion.create(
            api_key=self.openai_api_key,
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.system_description},
                {"role": "user", "content": self.word},
            ],
        )["choices"][0]["message"]["content"]
        if output == "na":
            print("Unable to find a definition and info for that word.")
            exit()

        try:
            output = json.loads(output)
            self.word = output["word"].title()
            self.part_of_speech = {
                "noun": "noun",
                "adjective": "adj",
                "verb": "verb",
                "adverb": "adverb",
                "pronoun": "pronoun",
                "preposition": "preposition",
            }[output["part_of_speech"].lower()]
            self.pronunciation = output["pronunciation"].lower()
            self.definitions = [definition.lower() for definition in output["definitions"]]
            self.synonyms = [synonym.lower() for synonym in output["synonyms"]]

            examples = []
            for example in output["examples"]:
                if example.endswith("."):
                    examples.append(example[:-1])
                else:
                    examples.append(example)
            self.examples = examples

        except json.decoder.JSONDecodeError:
            raise ValueError("Output is not valid JSON", output)

    def asDict(self) -> dict:
        return {attr: getattr(self, attr) for attr in self.WORD_ATTRS}


@dataclass(slots=True, frozen=True)
class Vocab:
    system_description: str
    openai_api_key: str

    def fetch_word(self, word: str) -> Word:
        """
        Fetches metadata about a word.

        Args:
            word: The word to fetch metadata about.

        Returns:
            A Word object containing the metadata about the word.
        """
        return Word(
            word=word,
            openai_api_key=self.openai_api_key,
            system_description=self.system_description,
        )

    def fetch_image(
        self,
        word: str, 
        filepath: str, 
        count: int = 2, 
        prompt: str | None = None
    ) -> None:
        """
        Fetch an AI generated image of the word and saves it to a filepath

        Arg:
            word: The word to fetch the image of.
            filepath: The filepath to save the image to.
            count: Number of images to generate.
            prompt: The prompt to use for the image. Automatic prompts are generated 
                if None is provided.

        Returns:
            None (saves the image to the filepath)
        """
        output = openai.Image.create(
            api_key=self.openai_api_key,
            prompt=prompt or f"Create a detailed painting of an object or a scene that represents the meaning of {word}. The image should convey the essence of the word and help me remember its meaning.",
            n=4,
            size="1024x1024",
            response_format="b64_json",
        )
        for i in range(count):
            with open(f"{filepath[:filepath.find('.')]}-{i+1}.png", "wb") as imageFile:
                imageFile.write(base64.b64decode(output["data"][i]["b64_json"]))

    def fetch_audio(self, word: str, filepath: str, slow: bool = True) -> None:
        """
        Fetch audio reading of the word and save it to a filepath

        Arg:
            word: The word to fetch the audio reading of.
            filepath: The filepath to save the audio file to.
            slow: Whether to have the reading be slow.

        Returns:
            None (saves the audio to the filepath)
        """
        gTTS(text=f". {word}", lang="en", tld="ca", slow=slow).save(filepath)
