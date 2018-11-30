import random
import re

def hangman_print(wrong_guess):
    switcher={
        0: "\n_________\n|       |\n|       \n|       \n|       \n|       \n|        ",
        1: "\n_________\n|       |\n|       O\n|       \n|       \n|       \n|        ",
        2: "\n_________\n|       |\n|       O\n|       |\n|        \n|       \n|        ",
        3: "\n_________\n|       |\n|       O\n|       |\n|       | \n|       \n|        ",
        4: "\n_________\n|       |\n|       O\n|       |\n|      /| \n|       \n|        ",
        5: "\n_________\n|       |\n|       O\n|       |\n|      /|\ \n|       |\n|       ",
        6: "\n_________\n|       |\n|       O\n|       |\n|      /|\ \n|       |\n|      /  ",
        7: "\n_________\n|       |\n|       O\n|       |\n|      /|\ \n|       |\n|      / \ \n ",
    }
    print switcher.get(wrong_guess);

def print_blanks(word):
    for i in range(len(word)):
            print"_",
            guessed_letters.append("_")
    print "\n"

def print_current(guessed_letters):
    for y in range(len(guessed_letters)):
        print guessed_letters[y],

def welcome():
    print "Let's play some hangman!"
    print "I have picked a random word"
    print "Guess the word before the man is fully drawn"

duplicate_letters=[];
letter_positions=[];
guessed_letters =[];
number_of_wrong = 0;

with open('words.txt') as myfile:
    wordbank = myfile.read().splitlines()
word = random.choice(wordbank);
word = word.lower();
welcome();
print_blanks(word);

while(1):
    if "_" not in guessed_letters:
        print "You guessed it!"
        exit(1);

    print "Guess a letter: "
    letter = raw_input();
    if len(letter) > 1:
        print "Only one letter at a time please"
        continue;
    elif letter.isupper():
        print"Lower case only please"
        continue;
    elif not re.match("^[a-z]*$", letter):
        print "Only letters a-z allowed!"
        continue;

    if letter in duplicate_letters:
        print "You have guessed that letter before. Try again."
        continue;
    duplicate_letters.append(letter);

    index_of_letter = word.find(letter);

    if index_of_letter == -1: #CASE 1: Letter not found in word
        print_current(guessed_letters);
        print "\n" + letter + " is not in the word"
        number_of_wrong = number_of_wrong + 1;
        hangman_print(number_of_wrong);
        if number_of_wrong == 7:
            print "Game Over!"
            print "The word is "+ word;
            exit(0);
    else:                      #CASE2: Letter is in the word
        for x in range(len(letter_positions)):
            letter_positions.pop();
        for pos, char in enumerate(word):
            if char == letter:
                letter_positions.append(pos);
        for j in range(len(letter_positions)):
            index = letter_positions[j];
            guessed_letters[index] = letter;

        print_current(guessed_letters);
        hangman_print(number_of_wrong);

exit(0);