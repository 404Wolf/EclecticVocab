import json
import os
import shutil
from contextlib import suppress
from secrets import token_hex

import genanki

from anki.model.model import MODEL, DECK
from anki.utils import gen_html_list, gen_formatted_html


class Anki:
    """
    Anki flashcard deck generator.

    Generate valid Anki flashcards w/media given a list of words that have been
    previously generated.
    """
    def __init__(self, words: list[str]):
        """Initialize the Anki flashcard generator."""
        self.words = words

    def generate(self, filename="deck.apkg") -> None:
        # Make a container folder to store all media
        try:
            os.mkdir("export")
            os.mkdir("export/resources")
        except FileExistsError:
            os.remove("export")
            os.mkdir("export")
            os.mkdir("export/resources")

        # All the media for the words (images and audio)
        media_files = []
        for word in self.words:
            with open(f"outputs/{word}/data.json") as wordDataFile:
                wordData = json.load(wordDataFile)

                # Create names for the files
                image_src = f"{word}-{token_hex(6)}.png"
                audio_src = f"{word}-{token_hex(6)}.mp3"

                # Copy files into the resources folder
                shutil.copyfile(
                    f"outputs/{word}/image.png", f"export/resources/{image_src}"
                )
                shutil.copyfile(
                    f"outputs/{word}/audio.mp3", f"export/resources/{audio_src}"
                )

                definitions = gen_html_list(wordData["definitions"], list_type="ol")
                synonyms = gen_html_list(wordData["synonyms"], list_type="ul")
                examples = gen_html_list(
                    map(gen_formatted_html, wordData["examples"]),  # type: ignore
                    list_type="ul"
                )
                notes = ""

                DECK.add_note(
                    genanki.Note(
                        fields=(
                            wordData["word"],
                            definitions,
                            examples,
                            synonyms,
                            notes,
                            f"<img src='{image_src}'>",
                            wordData["pronunciation"],
                            f"sound:{audio_src}"
                        ),
                        model=MODEL
                    )
                )
                media_files.append(f"export/resources/{audio_src}")
                media_files.append(f"export/resources/{audio_src}")

        # Dump the deck to a file
        genanki.Package(
            DECK,
            media_files=tuple(media_files)
        ).write_to_file(filename)
