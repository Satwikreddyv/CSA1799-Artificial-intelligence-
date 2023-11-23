def introduction():
        print '''Welcome to Kevin's European Geography Quizzes. 
        Test your knowledge of European geography. \n'''
        difficulty = raw_input('''Do you want to play an easy, medium, or hard game? 
        Please type the number 1 for easy, 2 for medium, or 3 for hard.\n''' )
        game_chooser(difficulty)

    def game_chooser(difficulty):
        cursor = 0
        difficulty_choice = [easy_game(), medium_game(), hard_game()]
 #each element of the above list links to a procedure and starts one of the 
 #mini-games.
        while cursor < len(difficulty_choice):
            if difficulty != cursor:
                cursor += 1
            else: 
                difficulty_choice[cursor]
                break
