import random

options = ("rock", "paper", "scissors")
user_score = 0
computer_score = 0
running = True

while running:
    print("\n--- Rock Paper Scissors ---")
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ").lower().strip()

    print(f"\nYou chose: {player}")
    print(f"Computer chose: {computer}")

    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win!")
        user_score += 1
    else:
        print("You lose!")
        computer_score += 1

    print(f"Score -> You: {user_score} | Computer: {computer_score}")

    if input("\nPlay again? (y/n): ").lower().strip() != "y":
        running = False

print("\nThanks for playing!")
print("\nHope to see you soon!")
