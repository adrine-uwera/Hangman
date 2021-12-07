# Name of the game: ALU Hangman
# This program asks the user 10 questions about ALU

# This dictionary stores the questions as keys and answers to the questions as values.
questions_and_answers = {
    '1.When was ALU founded (year)?': ['2015'],
    '2.Who is the CEO of ALU?': ['FRED SWANIKER', 'SWANIKER FRED'],
    '3.Where are ALU campuses? (Separate your answers by "and") ': ['RWANDA AND MAURITIUS', 'MAURITIUS AND RWANDA'],
    '4.How many campuses does ALU have? (Write your answers in numerical form) ': ['2'],
    '5.What is the name of ALU Rwanda’s Dean?': ['GAIDI FARAJ', 'FARAJ GAIDI'],
    '6.Who is in Charge of Student Life? ': ['SILA OGIDI', 'OGIDI SILA'],
    '7.What is the name of our Lab? ': ['NIGERIA'],
    '8.How many students do we have in year 2 Cs? (Write your answers in numerical form) ': ['57'],
    '9.How many degrees does ALU offer? (Write your answers in numerical form) ': ['8'],
    '10.Where are the headquarters of ALU? ': ['MAURITIUS']
}


# This function tells the user the instruction of the ALU Hangman game.
def game_introduction():
    print('''
Welcome to ALU hangman.

This game will test your knowledge about ALU by answering 10 questions.    
Every time you miss a question, you are hanging your man.
If you miss six questions, your man dies and the game stops.

Good Luck! Enjoy the game.
''')


# This function asks the user to input their response to questions and assess their answer.
def answer_questions():
    is_pass = True  # will indicate that the user passed the game
    incorrect_answers = 0  # variable to track the number of incorrect answers from the user
    incorrect_answer_limit = 6  # variable representing the number of accepted incorrect answers from the user

    # This code loops through the questions and answers dictionary
    for question, answer in questions_and_answers.items():
        user_answer = input(f'{question}: ')  # print the questions and receive user's answer
        user_answer = user_answer.upper()    # convert the user's input to uppercase
        if user_answer in questions_and_answers[question]:  # check if the answer given by the user is correct
            print("You got it right!")
        else:                                                # when answer is incorrect
            incorrect_answers += 1                            # increment the number of incorrect answers
            print("You are hanging your man")

            # check if the user reached the limited incorrect answers
            if incorrect_answers == incorrect_answer_limit:
                print(" ")
                print('The man died.')
                print('Game over!')
                is_pass = False  # This will indicate that the user didn't pass the game
                break

    # This codes evaluate the overall scores of the game
    if incorrect_answers == 0:
        print(" ")
        print('Your man lives')
        print('Congratulations! You passed all the questions.')

    if 0 < incorrect_answers < incorrect_answer_limit:
        correct_answers = 10 - incorrect_answers  # 10 is the total number of questions in one game
        print('\nYour man lives')
        print(f"You got You got {correct_answers} correct answers and {incorrect_answers} incorrect answers\n")

    return is_pass


# This function arranges the order in which the above functions will be executed and
# will allow the user to have other rounds to answer the questions.
def start_game():
    passed = 0  # variable to track the number of games the user passed
    failed = 0  # variable to track the number of games the user failed
    try_answering = 'Y'  # variable to start the game and its value is 'Y' so as to execute the intial game
    is_answering = True  # will allow to loop through game rounds

    # controls the execution of the game and rounds (trials for the user)
    while is_answering:
        if try_answering.upper() == 'Y' or try_answering.upper() == 'YES' or try_answering.upper() == 'YEAH':
            if answer_questions():
                # if the function runs until the end the is_pass would still be true
                # hence the user will have passed
                passed += 1
            else:
                # if the function gets cut due to the user failed 6 questions, the is_pass would be false
                # hence the user will have failed the game
                failed += 1

            # This will allow the user to restart the game or exit the game
            try_answering = input(("Do you want to play again? Enter 'y' or 'yes' or 'yeah' to continue "
                                   "or enter any other key to exit:  "))

        # This will be displayed after the users opts not to play again
        else:
            games_played = passed + failed
            print(f"\nYou played {games_played} games")
            print(f'You passed {passed} games and you failed {failed} games')
            print("Thanks for Playing/n")
            break


# This function arranges how the order in which the above functions will be executed
# i.e. sets the layout of the program
def main():
    game_introduction()
    start_game()


# This code calls the 'main' function which will also call the other functions
if __name__ == '__main__':
    main()
