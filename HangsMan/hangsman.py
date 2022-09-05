from ast import And
from hashlib import new
from dictionary import Dictionary
from game import Game
import os
class Hangsman():
    games_played = int
    lifes = int
    dictionary = Dictionary()
    player_name = str
    total_score = int
    found_words = []
    playing = bool

    def __init__(self, player_name) -> None:
        self.lifes = 5
        self.player_name = player_name
        self.total_score = 0
        self.playing = True
    
    def menu(self):
        
        while self.playing and self.lifes > 0:
            os.system("clear")
            print (f"Hi {self.player_name}, you have {self.lifes} lifes left and a score of {self.total_score}\n")
            option = input("Select an option:\n1.New Game\n2.Edit dictionary\n3.Quit Game\n")
            if option.isdigit():
                option = int(option)
                if option == 1:
                    self.new_game()
                elif option == 2:
                    self.edit_dictionary()
                elif option == 3:
                    self.quit_game()
                else:
                    print("Opcion errada")
        print (f"Thanks for playing {self.player_name}, see you soon")
                
            
    def new_game(self):
        new_word = ""
        while self.dictionary.dictionary_len > 0 and self.dictionary.dictionary_len > len(self.found_words):
            new_word = self.dictionary.get_new_word()
            if new_word.word not in self.found_words:
                break
        if new_word == "":
            print(f"No tenemos mas palabras, Score final {self.total_score}")
            self.quit_game()
            return 0
        my_game = Game(new_word)
        os.system("clear")
        while my_game.end_game == False and my_game.completed == False :
            
            print(f"Adivina la plabra {self.player_name}!!\n")
            print(str(my_game.status_word))
            option = input("Selecione la opcion\n1.Ingresar una letra\n2.Ingrese la palabra\n3.Reiniciar juego, Las vidas no se reinician\n")
            if option.isdigit():
                option = int(option)
                if option == 1:
                    option_1 = input("Ingrese la letra:\n")
                    my_game.insert_new_letter(option_1)
                elif option == 2:
                    option_2 = input("Ingrese la palabra\n")
                    my_game.insert_word(option_2)
                elif option == 3:
                    my_game.restart_game()
                else:
                    print("Opcion errada")

        if my_game.end_game == True and my_game.completed == False:
            self.lifes -= 1
            if self.lifes == 0:
                print(f"Has acabado todas tus vidas, Score final {self.total_score}")
                self.quit_game()
                return 0

        elif my_game.end_game == True and my_game.completed == True:
            self.found_words.append(new_word.word)
            self.total_score += my_game.find_word.score
            
    def edit_dictionary(self):
        os.system("clear")
        option = input("Selecione la opcion\n1.Ingresar una nueva palabra\n2.Remover una palabra\n")
        if option.isdigit():
            option = int(option)
            if option == 1:
                option_1 = input("Ingrese la palabra a insertar:\n")
                self.dictionary.add_new_word(option_1)
            elif option == 2:
                option_2 = input("Ingrese la palabra a eliminar\n")
                self.dictionary.remove_word(option_2)
            else:
                print("Opcion errada")
    def quit_game(self):
        self.playing = False




def main():
    player_name = str(input("What is your name?"))
    hang_man_game = Hangsman(player_name)
    hang_man_game.menu()



if __name__ == "__main__":
    main()