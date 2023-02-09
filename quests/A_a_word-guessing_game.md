# Python for Linguists 2023

## Coding Quest A: A word-guessing game

**_Finish [Section 7](../exercises/07_if-clauses.md) before attempting this quest._**


**A.1.** In a script do `import random` and then `target = random.choice(['apple', 'pear', 'banana'])`. Verify that the variable `target` now contains a different random string each time you run the program.

**A.2.** ⭐ Continue the program by asking the user to enter a single character. The program should then check whether the character is in the target string, and print `hit!` or `miss!` accordingly. Make sure to check whether indeed a single alphabetical character was entered, and if not, give appropriate feedback.

**A.3.** Extend the program to give the player five turns (i.e., five opportunities to enter a single character and get feedback). (Since we have not learned about looping/repeating yet, feel free to just duplicate the crucial code five times.) Can you also print the number of turns the player has left?

**A.4.** When the player's turns run out, they get _one shot_ at guessing the entire word. Print an appropriate closing message depending on whether they managed to guess correctly.

**A.5.** ⭐ Modify your program to ridicule the player when they enter the same character twice. 

**A.6.** The square brackets expression at the start (`['apple', 'pear', 'banana']`) define a _list_ datastructure, about which we will learn more soon. For now, to make the game more interesting, just add some more words to the list.

**A.7.** No programming required, just conceptually: what sort of functionality would we need to turn this word-guessing game into something like the well-known 'hangman' game? In hangman, crucially, you get not just binary feedback on a character guess, but also the position(s) of the guessed character in the target string.