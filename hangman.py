import random
fail1 = "o"
fail2 = "o-"
fail3 = "o-+"
fail4 = "o-+-"
fail5 = "o-+--"
fail6 = "o-+--<"
fails = 0
# A list of words that
potential_words = ["elegant", "cutie", "lunchtime", "Otherstuff", "guess"]

word = random.choice(potential_words)
print(word)
word = word.lower()

# Make it a list of letters for someone to guess
list = ["_"]*len(word) # TIP: the number of letters should match the word
print(list)
# Some useful variables
maxfails = 6
while fails < maxfails:
	guess = input("Guess a letter!")
if len(guess) == 1 and guess in :
    for i in range(len(word)):
        if word[i] == guess:
            list[i]=guess
    #print("You got one!")
    #singletter=word.index(guess)
    #list[singletter:singletter]
    #print(word[single letter])
    # check if the guess is valid: Is it one letter? Have they already guessed it?
	# check if the guess is correct: Is it in the word? If so, reveal the letters!
print(current_word)
fails = fails+1
print("You have " + str(maxfails - fails) + " tries left!")
