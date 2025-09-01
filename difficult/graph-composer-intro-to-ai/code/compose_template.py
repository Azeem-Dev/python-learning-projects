import string


def get_words_from_text(text_path):
    with open(text_path, 'r') as file:
        text = file.read()

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


def main():

    pass
