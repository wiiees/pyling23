# Python for Linguists 2023

## 7. If-clauses (`if`, `elif`, `else`)

Effort profile: `▁▁▁▁▁▁▁▂▁▂▁▁▂▁▁▁▁▄▅▂▁▁▁▁▂▁▁▂▁▂▄▅` 



**7.1.** Create a Python script with the following, predict what it does and test your prediction:

```python
if 4 + 2 == 6:
    print('yes!')
```


**7.2.** Modify various things in the above example, e.g., what if you replace `==` by `=`? (Undo that.) What if you remove the colon `:`? (Undo that.) What if you change the condition (`4 + 2 == 6`) into something that is false?

- - - - - -
**Something to keep in mind:** The `if`-clause consists of a **header** `if 4 + 2 == 6:` and a **suite** `print('yes!')`, also called the **body** of the if-clause. We will see various other types of clauses later, always consisting of a header and a suite (e.g., for-loops and function definitions). The header of a clause always ends with a colon `:`. The suite/body typically starts on a new line, and must be indented.
- - - - -

**7.3.** What happens if you remove the indentation from the above code, that is, what if header and suite start at the same level?

**7.4.** What if you place the print statement on the same line as the if-statement, i.e., after the colon?

**7.5.** What is being printed by the following program:

```python
if 1 + 1 == 5:
    print('uuuuhm...')

print('print this!')
```

**7.6.** What happens if you indent the second print statement to the same level as the first print statement? (Undo that.) What if you replace the condition by something true? What happens if you remove the newline between the two statements? What if you indent the second print statement again, but now add several newlines between the two print statements?

- - - - - -
**Something to keep in mind:** _Indentation is meaningful_ in Python, whereas in most other programming languages it is only an optional style convention. It's main purpose is to unambiguously delineate where the body/suite of a clause starts and ends.
- - - - -

**7.7.** In your Python editor (or the interpreter), can you indent with the 'tab' key? Do these appear as proper tabs (large spaces) or are they automatically replaced by sequences of multiple normal, narrow spaces? In the latter case, you're safe; but if the former can happen, you need to pay extra attention: Python permits indentation either with tabs or with spaces, but not mixed within the same file.

**7.8.** ⭐ Write a program that, given a variable `n` with a number, tests if its value is odd, and if not, adds 1 to it and prints _I made it odd!_. Subsequently, regardless of whether it was originally even or odd, the program should always print the resulting value of `n`.

**7.9.** Can one if-clause be embedded in the body of another if-clause? Do you need double indentation at some point? Insert print statements at various places and levels of indentation in this code to track what happens.

**7.10.** ⭐ Write a program that, given a variable `name` containing a string, tests if the first letter is `a`, and, if so, prints _The first letter is 'a'!_. Subsequently, if _in_addition_ the second letter is `b`, it should (additionally) print _The word starts with 'ab'!_. Apply your program to a number of strings to test, such as _able_, _apple_ and _banana_.

⭐⭐7.108.** ⭐ If you did the previous exercise with nested if-clauses (one contained in the other), try to redo it without -- and vice versa.

**7.11.** Write a program that asks for the user's name, tests if it starts with a vowel, and if so, prints _You are a vowel person!_.

**7.12.** Are the headers `if True:` and `if False:` accepted by Python (together with a suitable body)? What do these conditions achieve?

**7.13.** ⭐ You can follow an if-clause with an else-clause, which consists of its head `else:` and one or more statements as a body. Use `else:` to expand the previous program to print _You are a consonant person!_ in the right circumstances. How do you need to indent the various lines for it to work?

**7.14.** Is your program robust to users (not) capitalizing their name?

**7.15.** Now write a program that basically does the same, but is coded in the reverse order: it first tests if the name starts with a _consonant_, and if so prints _You are a consonant person!_; otherwise print _You are a vowel person!_. 

**7.16.** Did you type a long string of all the consonants to solve the foregoing exercise? If so, could this be avoided?

**7.17.** Write a program that tests whether the value of a variable `n` is odd, if so print _Odd!_, and if not print _Even!_. (What happens if you feed this program a string instead of a number?)

**7.18.** ⭐⭐ Oops, our client requests a change: they want the program to print, on the same line as _Odd!/Even!_, whether the number `n` is greater than 10, equal to 10, or smaller than 10.

**7.19.** ⭐ Our client requests another feature: if the number is both odd and greater than ten, that's a very special case where it should print only _ALARM!!!_ and nothing else.


**7.20.** Python's `elif` is shorthand for `else, if`. Can you predict what the following program does?

```python
if n > 0:
    print('Positive!')
elif n == 0:
    print('Zero!')
else:
    print('Negative!')
```

**7.21.** Together, the if-clause, elif-clause and else-clause form a **compound clause**. Can you also have an `elif` or an `else` clause on its own, without the initial `if` clause? Can you have more than one `elif`? More than one `else`? Why (not)?

**7.22.** What happens if you specify a condition also in the `else` header, e.g., `else n < 0:`?

**7.23.** In an if-elif-else compound clause, what happens if one of the three clauses has an empty suite (e.g., delete or comment out (`#`) one of the print statements in the code above).


**7.24.** ⭐ We both flip a coin (outside Python), and manually store the outcomes in two boolean variables `coin1` and `coin2`. If both came up heads, print _We both won!_, if both came up tails, print _Play again._, if only the first comes up heads, print _Player one won._, if the second, print _Player two won._.

**7.25.** Does your code for the previous exercise contain nested if-clauses? Implement a version without nested if-clauses. Besides `elif`, you can also reduce nested ifs by combining your conditions using boolean operators like `and` and `or`.

- - - - - -
**Something to keep in mind:** Nested if-clauses are frowned upon as an 'anti-pattern' in programming, to be avoided because they make code difficult to read and maintain -- and this applies not only to `if`-clauses (e.g., `for`-clauses, to be introduced in Section 10).
- - - - -

**7.26.** How often does your coin-flip program check the variables `coin1` and `coin2`? If either variable is checked more than twice, you are checking more than you need to; try to simplify your code.

**7.27.** ⭐ Write a program that takes two strings as input from the user (one after the other). If either one is less than three characters long, it prints _Too easy, you are disqualified!_. Otherwise, and if the two strings are not equal but one string is contained in the other, it prints _Yay well done!_, otherwise _Nope_.

**7.28.** Conceptually (no programming required), what sort of functionality would we need to implement to be able to check that the words entered by the users are, say, proper English words? 

- - - - - -
**Something to keep in mind:** When some exercise says to 'write a program that ...', you can either create a new `.py` file (and make sure you subsequently run the new file), or continue working in an existing file from a previous exercise. As long as the previous code doesn't give errors, and doesn't take too long to run, etc., continuing in the same file is fine. Of course you can also comment-out (`#`) previous code. (Later we will learn how to better structure your files.)
- - - - -

**7.29.** ⭐ Write a program that takes a word as input from the user, and checks the first two characters: if one is a vowel and the other a consonant (in either order), create a new string where the two characters are swapped; otherwise leave the string unchanged. Print the resulting string. Can you think of an English word that turns into another proper English word?

**7.30.** ⭐⭐ Write a program that takes a word as input from the user, tests a number of things in a row, and prints a single line of appropriate feedback: 
- whether it starts with two vowels, with a single vowel, or with a consonant 
- whether it has an even or odd number of characters 
- if odd, what the middle character is, and if even, what the middle two characters are 
- whether it is a palindrome (hint: use string slicing).





-----

**_🐋 You are now ready for [Coding Quest A](../quests/A_a_word-guessing_game.md)!_**