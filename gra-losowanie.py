import random
import enum
class rand_game:
    def __init__(self):
        self.directions = enum.Enum("Directions","forward left right backward")
        self.prizes = ["gold chest", "silver chest", "bronze chest", "normal chest"]
        self.prizes_chance = [0.05, 0.1, 0.3, 0.5]
        print("welcome to my game")
        print("its too simple to make you have fun, but its for self education")
        pass
    def move(self, direction=1):
        #assign rewards to directions
        dirs_prize=[]
        for direction in self.directions:
            dirs_prize.append(self.draw_prize())
        print("Directions:")
        for dir in self.directions:
            print(f"{dir.value}: {dir.name}")
        players_move=input("where u want to go? choose direction!\n")
        print(dirs_prize[int(players_move)-1])
    def draw_prize(self):
        return random.choices(self.prizes,weights=self.prizes_chance)[0]
    
game=rand_game()
game.move()
