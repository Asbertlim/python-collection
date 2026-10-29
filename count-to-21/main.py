print("============================================")
print("            Welcome to CountTo21            ")
print("============================================\n")

print("Game Rules:\n 1. If you say 21, you are out!\n 2. Player can only add up to max of 3 and min of 1\n 3. Player should start first.\n")

def initialiseGame(play):
  if play == "yes":
    current = 0
    move = [1,2,3]
    win = [4, 8, 12, 16, 20]

    print(f"Robot: You can start.")
    while True:
      player = int(input("Numbers to add (1,2,3): "))
      if player not in move:
        print("Incorrect addition. Please try again.")
        continue
      else:
        for i in range(1, player + 1):
          print(f"You: {current + 1}")
          current += 1

        if current >= 21:
          current = 21
          print("Robot: Haha.. you lost! Better luck next time.")
        

      for i in win:
        if current < i:
          dif = i - current
          for j in range(1, dif + 1):
            current += 1
            print(f"Robot: {current}")
          break

        if current == 21:
          print("Robot: Oh no.. I lost. Congratulations!")

while True:
  choice = input("Would you like to continue (yes/no): ").lower()
  if choice == "yes":
    initialiseGame("yes")
  else:
    continue
