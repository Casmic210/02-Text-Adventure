#!/usr/bin/env python3
import sys, os, json
# Check to make sure we are running the correct version of Python
assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

# The game and item description files (in the same folder as this script)
game_file = 'game.json'


# Load the contents of the files into the game and items dictionaries. You can largely ignore this
# Sorry it's messy, I'm trying to account for any potential craziness with the file location
def load_files():
    try:
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(os.path.join(__location__, game_file)) as json_file: game = json.load(json_file)
        return game
    except:
        print("There was a problem reading either the game or item file.")
        os._exit(1)


def render(game,current):
    c = game[current]
    print("Good morning Detective. The body of Alan Turner was found at 7am this morning by an office employee, and Alan's coworker, Alice Smith. Headquaters wants to label this a suicide, but me and the Police are not so sure. investigate the scene, and when you think you know the whole truth come visit the POLICE station. In the meantime don't forget to check out the ROOF, the BODY, the CORONER, the ROAD, the PARKING lot, the CAMERAS, the SUSPECTS, the A OFFICE, and the S OFFICES.")
    print("You are at the " + c["name"])
    print(c["desc"])

def get_input():
    response = input("Where do you want to go?")
    response = response.upper().strip()
    return response

def update(game,current,response):
    c = game[current]
    for e in c["exits"]:
        if response == e["exit"]:
            return e["target"]
    return current
    

# The main function for the game
def main():
    current = 'BODY'  # The starting location
    end_game = ['POLICE']  # Any of the end-game locations

    game = load_files()

    while True:
        render(game,current)

        for e in end_game:
            if current == e:
                print("You and the Police deliberated and discovered that Alice Smith was the one who killed Alan. She invited him up to the roof late at night and purposely loosened the bolts on the railing the previous day. She strangled him and placed the unconcious body up against the broken fence until gravity took over. In order to take credit for her and Alan's project, Alice attempted to shift suspicions from herself to her ex Carson. This is why you should never have an office romance.")
                break #break out of the while loop

        response = get_input()

        if response == "QUIT" or response == "Q":
            break #break out of the while loop

        current = update(game,current,response)

    print("Thanks for playing!")

# run the main function
if __name__ == '__main__':
	main()