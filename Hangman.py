import random
def showword(word_list,len_guess_word):

    for i in range(1,len_guess_word):
        for pos, letter in word_list.items():
            print(str(pos) + ":" + letter)


dashes = "_"
spaces = " "

print(dashes * 60)
print(spaces * 18 + "Welcome to Hangman Game" + spaces * 19)
print(dashes * 60)

word_file = "./words.txt"
list_of_words = open(word_file).read().splitlines()
for x in range(1):
  guess_word = list_of_words[random.randint(1,601)]
  print(guess_word)

print(spaces * 18 + "Guess the word. It is " + str(len(guess_word)) + " lettered word" + spaces * 19)
print(spaces * 18 + "You are only allowed 7 guesses" + spaces * 10)
i=0
j=0

word_list = {}
while(i < 7):
    letter = input("Enter a letter: ")
    pos = guess_word.find(letter)
    if pos == -1:
        print(spaces * 18 + "the letter %s is not in the word"  %letter)
    else:
        word_list[pos+1] = letter
        print(spaces * 18 + "the letter %s is present in the word in the position - %d" %(letter, pos+1 ))
        j = j + 1
        showword(word_list,len(guess_word))

        # if len(guess_word) == pos + 1:
        #     print dashes * pos + letter
        # else:
        #     print dashes *
    i = i + 1
    if len(guess_word ) == j:
        break


print(dashes * 18 + "the word is %s"  %guess_word)
print(dashes * 60)
print(dashes * 60)


if word_list == {}:
    print(spaces * 18 + "you lost the game. You did not find any letter" + spaces * 10)
    print(dashes * 60)

elif len(word_list) == len(guess_word):
    print(spaces * 10 + "CONGRATULATIONS you won the game. You found all the letters" + spaces * 10)
    print(dashes * 60)

else:
    print(spaces * 18 + "you just found %d letters" %len(word_list) + spaces * 10)
    print(spaces * 18 + "the letters you found are : ")
    print(spaces * 18 + word_list)
    #for word in word_list:
     #   print dashes * 18 + word_list[word]
    print(dashes * 60)