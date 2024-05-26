
def treasure_island():
    questions = ["left or right? ", "swim or wait? ", "Which door? "]
    for index, question in enumerate(questions):
      move = input(question)
      if index == 0:
          if move.lower() != "left":
             return "Fall into a hole. Game Over."
      elif index == 1:
          if move.lower() != "wait":
              return "Attacked by trout. Game Over."
      elif index == 2:
          if move.lower() == "yellow":
              return "You Win!"
          elif move.lower() == "red":
              return "Burned by fire. Game Over."
          elif move.lower() == "blue":
              return "Eaten by beasts. Game Over."
          else:
              return "Game Over."

restart = True

while restart:
    print(treasure_island())
    restart = input("Do you want to play again? y, n")
    if restart != "y":
        restart = False

