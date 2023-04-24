import genanki

DECK_ID = 1653370327737
DECK_NAME = "Vocab"
DECK = genanki.Deck(DECK_ID, DECK_NAME)

MODEL_ID = 1607392319
MODEL_NAME = "English Vocab"
MODEL_STYLES = open("anki/model/styles.css").read()
MODEL_FRONT_TEMPLATE = open("anki/model/front_template.html").read()
MODEL_BACK_TEMPLATE = open("anki/model/back_template.html").read()
MODEL = genanki.Model(
    MODEL_ID,
    MODEL_NAME,
    fields=[
        {'name': 'Word'},
        {'name': 'Definition'},
        {'name': 'Example'},
        {'name': 'Synonyms'},
        {'name': 'Notes'},
        {'name': 'Image'},
        {'name': 'Pronunciation'},
        {'name': 'Audio'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': MODEL_FRONT_TEMPLATE,
            'afmt': MODEL_BACK_TEMPLATE,
            'css': MODEL_STYLES,
        }
    ]
)
