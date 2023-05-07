# The goal of this code is to create and run a quiz game in python using some key concepts learn throughout the semester
# First we define the different functions that will be used in this game.

def new_game(): 

    guesses = []
    correct_guesses = 0
    question_num = 1
    
    # display all the questions in the library using a for loop
    # the dashes seperate the questions
    
    for key in library:
        print("---------")
        print(key)
     # show the options possible for each question using a nested for loop
     # this ensures that not all the answers to all the questions are shown, only that for the specific question
       
       for i in options[question_num-1]"
            print(i)
            
      # for user input, the user is required to type capital leters A-D
      
        guess = inpute("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guessess.append(guess)
        
        correct_guessess += check_answer(questions.get(key),guess)
        
       # to increment the question number each time  
       
        question_num += 1 
        
     # to display a final score
     
     display_score(correct_guesses, guesses)
     
## new class function 

def check_answer(answer, guess):

# check if the answer is the same as the guess 
    
    if answer == guess:,
    
    # message displayed to the user 
    
         print("CORRECT ANSWER!")
         
         # point attributed to the user for the correct answer 
         
          return 1 
            
       else:
           print("WRONG ANSWER!")
           return 0 
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



           
