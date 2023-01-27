import random as random
play_again="Y"
while play_again=="Y":
  my_file = open("usaWords.txt", "r")
  data = my_file.read()
  # replacing end splitting the text 
  # when newline ('\n') is seen.
  word_list = data.split("\n")
  my_file.close()
  #generating a random number
  random_word=(random.choice(word_list))
  #re-generating a random word if words are less than 5
  while len((random_word)) !=5:
      random_word=(random.choice(word_list))
  print('\u001b[47;1m' + '\033[31m'+'Welcome to Wordle! You have six chances to guess the five-letter word. A letter G means you got that letter correct and in the right position. A letter Y means you matched that letter, but it is in the wrong position.A letter B means that letter does not appear in the correct word')

      #Docstring required within each function:
  #     """
  #         Description of function: This function will repeat the input by user until they input properly. 
  #         return: user_guess.
  #     """
  def user_input():
      user_guess=input('Please enter your guess: ')
      guess_bad=True # Repeating below until the user gives a good input
      while guess_bad:
        if len(user_guess) !=5: #this should make sure that all digits can be converted to integers!
            print('Must contain five letters or more.')
            user_guess = input('Please enter a 5-letter word:')
        # elif len(set(str(user_guess))) <5:
        #         print('No duplicates.')
        #         user_guess = input('Please enter a 5-letter word. No duplicates:')
        else:
          guess_bad=False
      return user_guess
  #Docstring required within each function:
      """
          Description of function: This function will convert the words into lists to compare and output the answer to user. It also takes in the number of tries and outputs the count.
          return: The number of tries, and the past guesses. 
      """

 
  def add_user_lists(colored_guesses, past_guess)->int: 
    #I experiment with ANSI escape codes by changing the background color of the game. 
    background='\u001b[47;1m'
    
    user_guess=user_input()
    random_word_list=[]
    past_guess.append(user_guess)
    user_input_list=[]
    for letter in str(random_word):
      random_word_list.append(letter)
    for letter in str(user_guess):
      user_input_list.append(letter)
  #   Just to check the answers:  
    # print(random_word_list)
    # print(user_input_list)
    colored_guess=['B','B','B','B','B']

    #replacing the list with user tries
    for i in range (0, len(random_word_list)):
      if random_word_list[i]==user_input_list[i]:
        colored_guess[i]='G'
        random_word_list[i]='*'
        user_input_list[i]='-'
    for i in range(len(random_word_list)):
      if user_input_list[i] in random_word_list:
        index=random_word_list.index(user_input_list[i])
        random_word_list[index]='*'
        user_input_list[i]='-'
        colored_guess[i]='Y'
      
      elif user_input_list[i] not in random_word_list and random_word_list[i]!=user_input_list[i]:
        colored_guess[i]='B'
    # print(random_word_list)
    # print(user_input_list)
#adding the guesses in the guesses list to display to the user
    colored_guesses.append(colored_guess)

    for i in range(len(past_guess)):
    
      print(f"{background} Guess {i+1} is {past_guess[i]} colors are {''.join(colored_guesses[i])}")
    
    return colored_guesses

  #will store user guesses
  colored_guesses=[]
  #num of tries
  temp=[]
  #user's past guesses
  past_guess=[]
  while len(temp)<6 and ['G','G','G','G','G'] not in temp:
    temp=add_user_lists(colored_guesses, past_guess)
  if len(temp) >=6:
    print("You lost.")
  elif ['G','G','G','G','G'] in temp:
    print(f'you won! it took {len(temp)} tries!')
  play_again=(input("Do you want to play again? Y if yes, N if no: "))

