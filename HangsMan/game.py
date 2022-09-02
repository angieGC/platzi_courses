import unicodedata
# unicodedata.normalize('NFKD', string_1).encode('ASCII', 'ignore').strip().lower()
class Game:
    letters_used = []
    letters_left = []
    letters_word = []
    find_word = str
    completed = bool
    _lifes = int
     
    def __init__(self,word) -> None:
        self._lifes = 8
        self.completed = False
        self.end_game = False
        self.find_word = word
        self.letters_word = list(word.remove(" "))
        self.letters_left =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def restart_game(self):
        self.letters_left =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.letters_word = list(self.word.remove(" "))
    
    def insert_new_letter(self, input_letter):
        input_letter = unicodedata.normalize('NFKD', input_letter.remove(" ")).encode('ASCII', 'ignore').strip().lower()
        if len(input_letter) != 1 or input_letter.isdigit():
            print(f"Ingresa una sola letra sin números: {input_letter}")
        elif input_letter in self.letters_left and input_letter in unicodedata.normalize('NFKD', self.find_word.remove(" ")).encode('ASCII', 'ignore').strip().lower():
            print(f"La letra {input_letter} SI se encuentra en la palabra")
            self.letters_left = [i for i in self.letters_left if i != input_letter]
            self.letters_word = [i for i in self.letters_word if i != input_letter]
            if len(self.letters_word) == 0:
                print(f"Completaste la palabra {self.find_word}")
            if len(self.letters_left) == 0:
                print(f"Utilizaste todas las letras")
                self.completed = True
                self.end_game = True
        elif input_letter in self.letters_left:
            print(f"La letra {input_letter} NO se encuentra en la palabra")
            self._lifes -= 1
            if self.lifes == 0:
                self.end_game = True
            self.letters_left.pop(self.letters_left.get(input_letter))
        else:
            print(f"la letra {input_letter} ya fue usada")
    def insert_word(self, input_word):
        input_word = unicodedata.normalize('NFKD', input_word.remove(" ")).encode('ASCII', 'ignore').strip().lower()
        if len(input_word) < 3 or input_word.isdigit():
            print(f"Ingresa palabras de mas de 2 letras sin números: {input_word}")
        elif input_word == unicodedata.normalize('NFKD', self.find_word.remove(" ")).encode('ASCII', 'ignore').strip().lower():
            print(f"Correcto la palabra es {self.find_word}!!")
            self.end_game = True