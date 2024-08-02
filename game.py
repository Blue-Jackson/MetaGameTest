# Game: Cursed Temple

# Player starts with 100 health
health = 100

# Game loop
while health > 0:
  # Display player health
  print(f"Health: {health}")
  
  # Ask player what to do
  action = input("Do you want to (1) explore, (2) rest, or (3) quit? ")
  
  # Handle player action
  if action == "1":
    # Explore: 20% chance of losing 10 health
    import random
    if random.random() < 0.2:
      health -= 10
      print("You were injured!")
    else:
      print("You found a treasure!")
  elif action == "2":
    # Rest: gain 10 health
    health += 10
    print("You rested.")
  elif action == "3":
    # Quit: exit game
    print("Thanks for playing!")
    break
  else:
    # Invalid action: display error
    print("Invalid action. Try again!")

# Game over
print("Game over. You died!")
