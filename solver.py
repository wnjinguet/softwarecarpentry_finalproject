#The goal of this code is to create and run a quiz game in python using some key concepts learn throughout the semester
#First we define the different functions that will be used in this game.

def new_game(): 

    guesses = []
    correct_guesses = 0
    question_number = 1
    
    # display all the questions in the library using a for loop
    # the dashes seperate the questions
    
    for key in library:
        print("---------")
        print(key)
     # show all the options possible for each question using a nested for loop
        for i in options:
            print(i)
     
def check_answer():
  pass
def display_score():
  pass
def play_again():
  pass

# create a library of questions to be asked during the game
library = {
"A very high value of K indicates that: ": "B",
"What is the pH of a 10–5 M KOH solution?: ": "C",
"Active metals react with certain acids, such as hydrochloric acid, to yield a metal compound and: ": "A",
"How many moles of ions are produced by the dissociation of 1 mol of MgCl2? : ": "D",
"For the reaction represented by the equation 2H2 + O2 → 2H2O, how many grams of water are produced from 6.00
mol of hydrogen?: ": "B",
"Which of the following is an electrolyte?: ": "A",
}

# create a list of list. Each list corresponds to a value in the library of questions that were previously created 

answers = [["A. reactants are favored", "B. equilibrium is reached slowly", "C. products are favored", "D. equilibrium has been reached"],
          ["A. 5", "B. 3", "C. 9", "D. 11"],
          ["A. chlorine", "B. oxygen", "C. hydrogen", "D. sodium"],
          ["A. 0, "B. 2 mol", "C. 3 mol", "D. 1 mol"],
          ["A. 108 g", "B. 2.00 g", "C. 6.00 g", "D. 54.0 g"],
          ["A. glass", "B. sugar", "C. sodium chloride", "D. pure water"],
          
# create a new game by calling the new game function



           
