import json
from random import randint
import genanki

def gen_id() -> int:
    """Generate a deck id."""
    return randint(1000000000, 9999999999)

class Anki:
    """
    Anki flashcard deck generator.

    Generate valid Anki flashcards w/media given a list of words that have been
    previously generated.
    """
    MODEL = genanki.Model(
        gen_id(),
        "Vocab Word",
        fields=[
            {'name': 'Word'},
            {'name': 'Definitions'},
            {'name': 'Synonyms'},
            {'name': 'Examples'},
        ]
    )

    def __init__(self, words: list[str]):
        """Initialize the Anki flashcard generator."""
        self.words = words

    def generate(self, filename="deck.apkg") -> None:
        # Create the deck with the Vocab words
        deck = genanki.Deck(2059400110, "Vocab Words")

        for word in self.words:
            with open(f"outputs/{word}/data.json") as wordData:
                wordData = json.load(wordData)
                deck.add_note(
                    wordData["word"]
                )

        genanki.Package(deck).write_to_file(filename)
