from words import Words
import unidecode
from random import randint

class Dictionary:
    actual_words = []
    dictionary_len =  int

    def __init__(self) -> None:
        with open("/home/familiagc/Documentos/Angie/POO/Python/archivos/words.txt","r", encoding="utf-8") as f:
            for line in f:
                self.actual_words.append(Words(line.strip("\n")))
        self.dictionary_len = len(self.actual_words)
        
    
    def add_new_word(self, input_word):
        if len(input_word) < 3 or any(chr.isdigit() for chr in input_word):
            print(f"Ingresa palabras de mas de 2 letras sin números {input_word}")
        else:
            result = [line for line,i in enumerate(self.actual_words) if unidecode.unidecode(i.word).strip().lower() == unidecode.unidecode(input_word).strip().lower()]
            if len(result) == 0:
                self.actual_words.append(Words(input_word))
                with open("/home/familiagc/Documentos/Angie/POO/Python/archivos/words.txt","a", encoding="utf-8") as f:
                    f.write("\n")
                    f.write(input_word)
                self.dictionary_len += 1
                print(f"Se ha insertado la palabra {input_word}")
            else:
                print(f"La palabra {input_word} ya existe")


    def remove_word(self, input_word):
        result = [line for line,i in enumerate(self.actual_words) if unidecode.unidecode(i.word).strip().lower() == unidecode.unidecode(input_word).strip().lower()]
        lines = []
        if 0 != len(result):
            print(f"Se ha eliminado la palabra {input_word}")
            for i in result[::-1]:
                self.actual_words.pop(i)
            self.dictionary_len = len(self.actual_words)
            with open(r"/home/familiagc/Documentos/Angie/POO/Python/archivos/words.txt", 'r', encoding="utf-8") as fp:
                lines = fp.readlines()
            with open(r"/home/familiagc/Documentos/Angie/POO/Python/archivos/words.txt", 'w', encoding="utf-8") as fp:
                for number, line in enumerate(lines):
                    if number not in result:
                        fp.write(line)
        else:
            print(f"No ha encontrado la palabra {input_word}")

    def get_new_word(self,):
        index_word =  randint(0,self.dictionary_len-1)
        return self.actual_words[index_word]
