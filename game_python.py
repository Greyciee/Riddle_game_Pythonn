# Simple Riddle Game with User Input

# List of riddles and their answers (extended with more fun and common riddles)
riddles = {
    "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?": "echo",
    "You measure my life in hours and I serve you by expiring. I’m quick when I’m thin and slow when I’m fat. The wind is my enemy. What am I?": "candle",
    "The more of this there is, the less you see. What is it?": "darkness",
    "What has keys but can’t open locks?": "piano",
    "What has hands but can’t clap?": "clock",
    "What has to be broken before you can use it?": "egg",
    "I’m tall when I’m young, and I’m short when I’m old. What am I?": "candle",
    "What month of the year has 28 days?": "all of them",
    "What is full of holes but still holds water?": "sponge",
    "What question can you never answer yes to?": "are you asleep",
    "What is always in front of you but can’t be seen?": "future",
    "There’s a one-story house in which everything is yellow. Yellow walls,yellow doors, yellow furniture. What color are the stairs?": "no stairs",
    "What can you break, even if you never pick it up or touch it?": "promise",
    "What goes up but never comes down?": "age",
    "A man who was outside in the rain without an umbrella or hat didn’t get a single hair on his head wet. Why?": "he was bald",
    "What gets wet while drying?": "towel",
    "I shave every day, but my beard stays the same. What am I?": "barber",
    "You see a boat filled with people. It has not sunk, but when you look again you don’t see a single person on the boat. Why?": "all the people were married",
    "What can’t talk but will reply when spoken to?": "echo",
    "The more you take, the more you leave behind. What are they?": "footsteps"
}

# Game introduction
print("Welcome to the Riddle Game!")

# Ask the user for their name
user_name = input("Please enter your name: ")

# Welcome the user personally
print(f"Hello {user_name}, it's great to have you here!")
print("You'll be solving some fun riddles today.")

# Ask the user how many riddles they'd like to solve
num_riddles = int(input("How many riddles would you like to solve? (Max: 20): "))

# Limit the number of riddles to the available ones
num_riddles = min(num_riddles, len(riddles))

# Game begins
print(f"Alright {user_name}, let's begin! You'll solve {num_riddles} riddles. Type 'exit' to quit anytime.")

# Initialize the score
score = 0

# Game loop to ask riddles
riddles_asked = 0
for riddle, answer in riddles.items():
    if riddles_asked >= num_riddles:
        break

    print("Riddle:", riddle)
    # Convert user's input to lowercase to make it case-insensitive
    user_answer = input("Your answer: ").strip().lower()

    if user_answer == "exit":
        break

    # Check answer by converting both user input and correct answer to lowercase
    if user_answer == answer.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is: {answer}")

    riddles_asked += 1

# Final score
print(f"Game Over! you solved {score} out of {num_riddles} riddles correctly WELDONE {user_name}!")
