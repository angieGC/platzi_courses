from words import Words
import unicodedata

class Dictionary:
    actual_words = []
    dictionary_len =  int

    def __init__(self) -> None:
        with open("D:/Angie/python/POO/platzi_courses/archivos/words.txt","r", encoding="utf-8") as f:
            for line in f:
                self.actual_words.append(Words(line.strip("\n")))
        self.dictionary_len = len(self.actual_words)
        
    
    def add_new_word(self, input_word):
        if len(input_word) < 3 or any(chr.isdigit() for chr in input_word):
            print(f"Ingresa palabras de mas de 2 letras sin números {input_word}")
        else:
            self.actual_words.append(Words(input_word))
            with open("D:/Angie/python/POO/platzi_courses/archivos/words.txt","a", encoding="utf-8") as f:
                f.write("\n")
                f.write(input_word)
            self.dictionary_len += 1
            print(f"Se ha insertado la palabra {input_word}")

    def remove_word(self, input_word):
        result = [line for line,i in enumerate(self.actual_words) if unicodedata.normalize('NFKD', i.word).encode('ASCII', 'ignore').strip().lower() == unicodedata.normalize('NFKD', input_word).encode('ASCII', 'ignore').strip().lower()]
        lines = []
        if 0 != len(result):
            print(f"Se ha eliminado la palabra {input_word}")
            for i in result[::-1]:
                self.actual_words.pop(i)
            self.dictionary_len = len(self.actual_words)
            with open(r"D:/Angie/python/POO/platzi_courses/archivos/words.txt", 'r', encoding="utf-8") as fp:
                lines = fp.readlines()
            with open(r"D:/Angie/python/POO/platzi_courses/archivos/words.txt", 'w', encoding="utf-8") as fp:
                for number, line in enumerate(lines):
                    if number not in result:
                        fp.write(line)
        else:
            print(f"No ha encontrado la palabra {input_word}")