import unidecode
class Game:
    letters_used = []
    letters_left = []
    letters_word = []
    find_word = str
    completed = bool
    end_game = bool
    _lifes = int
     
    def __init__(self,word) -> None:
        self._lifes = 8
        self.completed = False
        self.end_game = False
        self.find_word = word
        self.letters_word = list(word.word.replace(" ",""))
        self.letters_left =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.status_word = ['_ ' for i in range(len(word.word.replace(" ","")))]

    def restart_game(self):
        self.letters_left =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.letters_word = list(self.word.word.replace(" ",""))
        self.status_word = ['_ ' for i in range(len(self.word.word.replace(" ","")))]
    
    def insert_new_letter(self, input_letter):
        input_letter = unidecode.unidecode(input_letter.replace(" ","")).strip().lower()
        if len(input_letter) != 1 or input_letter.isdigit():
            print(f"Ingresa una sola letra sin números: {input_letter}")
        elif input_letter in self.letters_left and input_letter in str(unidecode.unidecode(self.find_word.word.replace(" ","")).strip().lower()):
            print(f"La letra {input_letter} SI se encuentra en la palabra")
            self.letters_left = [i for i in self.letters_left if i != input_letter]
            self.letters_word = [i for i in self.letters_word if i != input_letter]
            actual_word = unidecode.unidecode(self.find_word.word.replace(" ","")).strip().lower()
            for i in range(len(actual_word)):
                if actual_word[i] == input_letter:
                    self.status_word[i] = self.find_word.word.replace(" ","")[i]
            if len(self.letters_word) == 0:
                print(f"Completaste la palabra {self.find_word}")
                self.completed = True
                self.end_game = True
            if len(self.letters_left) == 0:
                print(f"Utilizaste todas las letras")
                self.end_game = True
        elif input_letter in self.letters_left:
            print(f"La letra {input_letter} NO se encuentra en la palabra")
            self._lifes -= 1
            if self._lifes == 0:
                self.end_game = True
            self.letters_left = [i for i in self.letters_left if i != input_letter]
        else:
            print(f"la letra {input_letter} ya fue usada")
        print (f"you have {self._lifes} lifes\n")

    def insert_word(self, input_word):
        input_word = unidecode.unidecode(input_word.replace(" ","")).strip().lower()
        if len(input_word) < 3 or input_word.isdigit():
            print(f"Ingresa palabras de mas de 2 letras sin números: {input_word}")
        elif input_word == unidecode.unidecode(self.find_word.word.replace(" ","")).strip().lower():
            print(f"Correcto la palabra es {self.find_word.word}!!")
            self.completed = True
            self.end_game = True
        else:
            print(f"Incorrecto la palabra {input_word} no es la que buscas!!")
            self._lifes -= 1
            if self._lifes == 0:
                self.end_game = True
        print (f"you have {self._lifes} lifes\n")