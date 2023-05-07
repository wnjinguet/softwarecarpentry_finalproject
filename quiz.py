# The goal of this code is to create and run a quiz game in python using some key concepts learned throughout the semester
# First we define the different functions that will be used in this game.

import matplotlib.pyplot as plt

def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    # display all the questions in the library using a for loop
    # the dashes seperate the questions
    
    for key in questions:
        print("-------------------------")
        print(key)

        # show the options possible for each question using a nested for loop
        # this ensures that not all the answers to all the questions are shown, only that for the specific question
       
        for i in options[question_num-1]:
            print(i)

        # for user input, the user is required to type capital leters A-D

        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)

        # to increment the question number each time  

        question_num += 1
    
    # to display a final score

    display_score(correct_guesses, guesses)

# new class funtion

def check_answer(answer, guess):

# check if the answer is the same as the guess 

    if answer == guess:
        print("CORRECT ANSWER!")

        # the point attributed to the user for the correct answer 

        return 1
    else:
        print("INCCORECT ANSWER!")
        return 0

# new class function

def display_score(correct_guesses, guesses):

     # the lines seperate the questions and answers

    print("----------------")
    print("RESULTS")
    print("----------------")
    print("Answers: ", end="")

    # to show all the answers, using a for loop

    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    # to calculate the final score

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

# new class function

def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False


# create a library of questions to be asked during the game

questions = {
"A very high value of K indicates that: ": "B",
"What is the pH of a 10–5 M KOH solution?: ": "C",
"Active metals react with certain acids, such as hydrochloric acid, to yield a metal compound and: ": "A",
"How many moles of ions are produced by the dissociation of 1 mol of MgCl2? : ": "D",
"Which of the following is an electrolyte?: ": "A",
}

# create a list of list. Each list corresponds to a value in the library of questions that were previously created 

options = [["A. reactants are favored", "B. slow equilibrium is reached slowly", "C. products are favored", "D. equilibrium has been reached"],
          ["A. 5", "B. 3", "C. 9", "D. 11"],
          ["A. chlorine", "B. oxygen", "C. hydrogen", "D. sodium"],
          ["A. 108 g", "B. 2.00 g", "C. 6.00 g", "D. 54.0 g"],
          ["A. glass", "B. sugar", "C. sodium chloride", "D. pure water"]]

# create a new game by calling the new game function

new_game()

while play_again():
    new_game()

# to give feedback to the player

score = float(input("Enter your quiz score (out of 100): "))

if score >= 75:
    print("Congratulations! 🥳 You scored 75% or higher!")
else:
    print("Sorry, you didn't score 75% or higher. Keep practicing!🙂")

new_game()

while play_again():
    new_game()

new_game()

while play_again():
    new_game()

print("The End!")

# to graph the scores

scores = []

# Ask the user to enter scores
while True:
    try:
        score = int(input("Enter a score (or -1 to stop): "))
        if score == -1:
            break
        scores.append(score)
    except ValueError:
        print("Please enter a valid integer.")

# Generate the bar graph
plt.bar(range(len(scores)), scores)
plt.title("Scores")
plt.xlabel("Trial Number")
plt.ylabel("Score")
plt.show()


while play_again():
    new_game()

print("The End!")


           
