# Eclectic English Vocab
For the past few years, I've curated eclectic English vocab words into a spaced repetition flashcard deck. For each word, I've manually searched up definitions, synonyms, images, pronunciation, and more. This project is aimed at streamlining that process, to automatically compile data for given words.

## How?
<image align="right" width="30%" src="https://user-images.githubusercontent.com/108041238/234724038-ce4a52e3-a0d4-4afa-8ea2-a4cfcd572844.png" alt="Adding a flashcard"/>
For each flashcard, there are 9 different fields: word, definitions, examples, synonyms, notes, images, pronunciation, audio, and part of speech. All fields are needed for every card except notes, which is reserved for when an important note is needed to provide context for a word. This project implements OpenAI's natural language generating ChatGTP API and image generating DALLE API, along with Google text to speech, to generate all the needed data to create an English flashcard.
