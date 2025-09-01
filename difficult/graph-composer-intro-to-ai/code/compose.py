import random
import re
import string
from graph import Graph, Vertex
import os


def get_words_from_text(text_path):
    with open(text_path, 'r') as file:
        text = file.read()

        text = re.sub(r'\[(.+)\]', '', text)

        text = ' '.join(text.split())
        """
        THE ABOVE LINE OF CODE I.E.  -> text = ' '.join(text.split())
        WHAT IT DOES IS THAT REMOVE ALL/ANY WHITESPACES, NEW LINES, TABS ETC TO JUST A SIMPLE WHITE SPACE.
        
        EXAMPLE:
        
        text that looks
        like
        
        this
        
        NEW BECOMES:
        
        text that looks like this
        
        """
        text = text.lower()

        text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    return words


def make_graph(words):
    g = Graph()

    previous_word: Vertex | None = None
    for word in words:
        word_vertex = g.get_vertex(word)
        if previous_word:
            previous_word.increment_edge(word_vertex)

        previous_word = word_vertex

    g.generate_probability_mappings()

    return g


def compose(g, words, length=50):
    composition = []
    word = g.get_vertex(random.choice(words))
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)

    return composition


def main(artist: str):

    words = []

    """FOR SONGS"""
    for song_file in os.listdir(f'songs/{artist}'):
        if song_file == '.DS_Store':
            continue

        song_words = get_words_from_text(f'songs/{artist}/{song_file}')
        words.extend(song_words)

    """FOR TEXTS"""
    # words = get_words_from_text('texts/hp_sorcerer_stone.txt')

    g = make_graph(words)

    compostion = compose(g, words, 100)

    return ' '.join(compostion)


if __name__ == "__main__":
    print(main('halsey'))
