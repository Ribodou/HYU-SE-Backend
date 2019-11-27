from bottle import run
import bottles_functions



if __name__ == "__main__":
    run(bottles_functions.app, host="0.0.0.0", port=8081, quiet=True)


# ai_module            | AIs classes
# bottles_functions    | server related function
# errors               | error classes
# game_logic_functions | functions related to the logic of the game
# main                 | file that lauches the system