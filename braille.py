def main():
    # user input lyrics to song
    lyrics = input("Enter the lyrics to be translated to Braille: ").lower()
    print(convert_lyrics(lyrics))

    # user input musical notes to song
    notes = input("Enter the musical notes to be translated to Braille: ").lower()
    ind_note = notes.split(" ")  # splitting notes at the space
    element = [] 
    for note in ind_note:
        element.append(note)  # adding note into element space
    print(convert_notes(element))


def convert_lyrics(lyrics):
    # Braille alphabet dictionary (for lyrics)
    braille_letters = {
    # letters
    'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑',
    'f': '⠋', 'g': '⠛', 'h': '⠓', 'i': '⠊', 'j': '⠚',
    'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕',
    'p': '⠏', 'q': '⠟', 'r': '⠗', 's': '⠎', 't': '⠞',
    'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽', 'z': '⠵',
    # numbers
    '1': '⠼⠁', '2': '⠼⠃', '3': '⠼⠉', '4': '⠼⠙', '5': '⠼⠑',
    '6': '⠼⠋', '7': '⠼⠛', '8': '⠼⠓', '9': '⠼⠊', '0': '⠼⠚',
    # punctuation
    ' ': ' ', '.': '⠲', ',': '⠂', '?': '⠦', '!': '⠖', '-': '⠤',
    }

    # conversion of alphabet to braille letters
    lyrics = "".join(braille_letters.get(letter, letter) for letter in lyrics)
    return lyrics
    

def convert_notes(notes):
    # Braille musical note dictionary
    braille_music = {
    # note 
    'c': '⠉',
    'd': '⠙',
    'e': '⠑',
    'f': '⠋',
    'g': '⠛',
    'a': '⠁',
    'b': '⠃',
    # note duration
    'whole': '⠼⠴', 
    'half': '⠼⠦', 
    'quarter': '⠼⠲', 
    'eighth': '⠼⠢', 
    'sixteenth': '⠼⠂',
    # rests
    'whole_rest': '⠲',
    'half_rest': '⠴',
    'quarter_rest': '⠶',
    # accidentals
    'sharp': '⠮',
    'flat': '⠧',
    'natural': '⠵',
    # dynamics
    'forte': '⠋⠞',
    'piano': '⠏⠊',
    'crescendo': '⠉⠗',
    'decrescendo': '⠙⠑',
    # punctuation
    ' ': ' ', '.': '⠲', ',': '⠂', '?': '⠦', '!': '⠖', '-': '⠤',
    }

    braille_translate = ''
    for cell in notes:
        # looking up braille equivalent & using cell itself if not found
        braille_char = braille_music.get(cell, cell)
        # adding braille char to end of translation string w space for readability
        braille_translate += braille_char + ' '
    
    # trimming string to return
    return braille_translate.strip()


main()
