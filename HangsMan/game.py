import unicodedata
# unicodedata.normalize('NFKD', string_1).encode('ASCII', 'ignore').strip().lower()
class Game:
    letters_used = []
    letters_left = []
    letters_word = []
    find_word = str
     
    def __init__(self,word) -> None:
        self.find_word = word
        self.letters_word = word.remove(" ").split()
        self.letters_left =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def restart_game(self):
        self.letters_left =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.letters_left = []
    
    def insert_new_letter(self, letter):
        if unicodedata.normalize('NFKD', letter).encode('ASCII', 'ignore').strip().lower() in self.letters_left and unicodedata.normalize('NFKD', letter).encode('ASCII', 'ignore').strip().lower() in unicodedata.normalize('NFKD', self.find_word).encode('ASCII', 'ignore').strip().lower():
            print(f"la letra {letter} si se encuentra en la palabra")
            self.letters_left.pop(self.letters_left.get(unicodedata.normalize('NFKD', letter).encode('ASCII', 'ignore').strip().lower()))
            self.letters_used.append(unicodedata.normalize('NFKD', letter).encode('ASCII', 'ignore').strip().lower())
        elif unicodedata.normalize('NFKD', letter).encode('ASCII', 'ignore').strip().lower() in self.letters_left:
            self.letters_left.pop(self.letters_left.get(unicodedata.normalize('NFKD', letter).encode('ASCII', 'ignore').strip().lower()))
            self.letters_used.append(unicodedata.normalize('NFKD', letter).encode('ASCII', 'ignore').strip().lower())
