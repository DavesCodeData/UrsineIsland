from ursina import *
from intro import StartGame#import self created class for main_menu options
class Game:
    def __init__(self):
        print('init was called.............................................')
        self.start_game = StartGame()

    #run the start game class in the intro tab to select an intro button option
    def main_menu(self):
        self.StartGame()

if __name__ == '__main__':#run all code through this file in ursina
    app = Ursina()        #this is required to prevent multiple show bases
    game = Game()
    app.run()
    
  
