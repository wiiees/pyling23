# Python for Linguists 2023

## 20. Reading and writing files (`read`/`write`)

Effort profile: `▁▁▂▁▁▁▁▁▁▂▁▂▁▁▁▁▄▅▁▁▁▁▁▁▁▁▁▄▅▁▁▁▂▁▁▄▅▁▂` 



**20.1.** Without searching the web, try to gather and formulate your intuitions: What is a file? What is the difference between, and relation between, long-term storage (e.g., your hard-disk, or the cloud) and working memory (RAM)? What is a folder (or directory)? What is a path (such as, depending on your operating system, `C:\Documents\semantics_report.pdf` or `~/Downloads/Alice_in_wonderland.txt`)? What might be the difference between an _absolute_ and a _relative_ path?

- - - - - -
**Something to keep in mind:** ⚠️ Before executing any code that involves opening a file, _always assume the worst_: that the referenced file, if it exists, will be destroyed/overwritten. Make sure you do not lose valuable data in case this happens. Some things we will learn -- using a context manager, opening a file as 'read-only' where possible, using relative paths -- and in general clean code help decrease the chance of unintended changes to your files.
- - - - -

**20.2.** Create a Python script with the following code. Execute it, then find the created file `test123.txt` on your computer and open it (it will be in the same folder as your Python script). 

```python
with open('test123.txt', 'w') as file:
    file.write('Hello!')
```


**20.3.** ⭐ Experiment with the above code. What if, inside the `with`-block, you add a second write statement? What will be in the file if you repeat the entire `with`-block twice? Does a `with`-block create a local scope? Does this align with what happens if you try to write a bit more to the file _after_ (i.e., outside, non-indented) the `with`-block? Are you free to choose a different name for your file, e.g., `with open('test123.txt') as blablabla:`?

**20.4.** What if you omit the second argument of `open`, i.e., the string `'w'`? What if you replace it by an `'a'` and run the code several times? In each case inspect the resulting file.

**20.5.** Call `help(open)` and find the table explaining the different modes. Based on the previous exercise, what might be meant by 'truncating' in the explanation given for `w`?

**20.6.** Given a list of strings, use a loop inside the `with`-clause to write all strings to the file, each on a new line.

**20.7.** Assuming you now have a multi-line file `test123.txt`, execute the following code to read it. Does `file.read()` read one character or one line at a time, or the full file contents at once?

```python
with open('test123.txt', 'r') as file:
    text = file.read()
print(text)
```


**20.8.** What happens if you try to read the same file with `read` twice in a row, _within a single `with`-block_ (and print the results of both reads)? What if you read the same file twice but in _separate_ `with`-blocks? Hypothesize about what may cause this difference.

**20.9.** The file method `read` optionally takes an integer argument. What does it do? Try it. Then form an expectation: what will happen if you call `read` repeatedly on the same file with this integer argument specified? First formulate your expectation, then test it.

**20.10.** ⭐ When you open a file, a pointer is kept that tracks the 'current position' in the file, i.e., the index of the byte of the file that is to be read next. In read-only mode `r`, this pointer starts at 0 (start of the file) and is incremented while the file is being read. Can you reconcile this with your findings in the previous two exercises? What will be the value of this pointer after reading an entire file? Calling `.tell()` on the file gives you the value of the pointer -- you can use this to test your prediction.

**20.11.** What do you think the starting value of the pointer of a file will be when you use append mode `a`? And what if you use write mode `w`? Again, test your predictions with the `tell` method.

- - - - - -
**Something to keep in mind:** If with Python code you want to read from or write to a file, you first need to **open** the file. The standard idiom uses the built-in function `open`, which takes a path and a _mode_ (read-only `r`, write-only `w`, read-and-write `r+`, append `a`) and returns a file object with methods such as `read` and `write` and a pointer to the 'current' position in the file. 
- - - - -

**20.12.** ⭐ Code you executed further above created the file `test123.txt`. Find this file in the Project tab on the left, and open it in the PyCharm editor (e.g., by double-clicking it). Can you manually change the contents of the file in the editor? Do they show up if you subsequently read the file in Python (of course you will not see this if your script overwrites the file prior to reading it)? And if you write something to the file through Python, does your view of the file in the editor update automatically?


**20.13.** As we have seen, opening a file in Python with `open` does not yet load the contents of the file into working memory. Instead, calling a method like `.read()` on an open file (or, e.g., iterating over it) is what actually loads the content. Is this similar to 'opening' a file in the way you are probably used to, e.g., opening a document in MS Word)?


- - - - - -
**Something to keep in mind:** The file `test123.txt` was created in the same directory that contains the Python script, because `open` was given a **relative path**, i.e., it specified the desired file location _relative to_ the directory of the current (main) script. An **absolute path** specifies the location of a file all the way from the root of your file-system or home directory (e.g., `C:\` in Windows, `~` on Mac, Linux).
- - - - -

**20.14.** What might be (dis)advantages of using absolute vs. relative paths?

**20.15.** Re-run some of the above code with different paths (though keep in mind the earlier warning about losing data!), including an _absolute_ path to a place on your disk (e.g., depending on operating system, `C:\Documents\test456.txt` or `~/Documents/test456.txt`), and a _relative_ path to a sub-folder of the current working directory, e.g., `output/test789.txt` (first manually create such a folder if none exists yet).

**20.16.** In PyCharm, you can right-click (or ctrl-click) on a file in the Project tab on the left, choose 'Copy path/reference' and select 'Absolute path' or 'Path from repository root'. Try this (copy, and then paste the copied path somewhere else, e.g., into a string in your Python script). If your Python script is in the repository root (i.e., not in a sub-folder), then the latter corresponds also to the _relative_ path from your Python script.

**20.17.** ⭐⭐ How does writing to and reading from a file, relate to other input/output methods we have already learned about so far? Consider `input`, `print` and `import`. Compare them both in terms of their intended purpose and in terms of the details of their usage. For instance, do `write` and `print` behave differently with regard to newlines? Does `write`, like `print`, allow non-string arguments? Does it allow multiple arguments? What if you `open` and `read` a python file instead of using `import`; is any of its code executed? Illustrate all of this with actual code; take your time!

**20.18.** You might be wondering what the `with`-keyword does. First, verify that the following code appears to work just as well:

```python
file = open('test123.txt', 'r')
text = file.read()
print(text)
```



**20.19.** After opening a file through Python, one should **close** it (because unintentionally leaving files open _can_ have some downsides). This is done with `file.close()`. Add this to the code from the previous exercise, and verify that it still works. In this simple setting, you will likely not notice any different behavior.


**20.20.** Do you expect the (content of the) variable `text` to still be available _after_ you close the file? Test this, and explain why (not) with reference to the distinction between long-term storage and working memory.


- - - - - -
**Something to keep in mind:** The keywords `with ... as ...`, which as we have seen are part of the standard idiom for opening files, create a **context manager** whose job it is to ensure that the opened file is automatically closed once the `with`-block ends (i.e., when you un-indent) or when an error is encountered.
- - - - -

**20.21.** What would be an advantage of using a context manager to open a file, as opposed to manually closing it as in the preceding exercises? 


**20.22.** In the following code, choose appropriate modes in place of the `...`, such that their respective files (assuming they do not exist yet) end up having the exact same content. What could be reasons for preferring one over the other?

```python
with open('testABC.txt', ...) as file:
    for i in range(10):
        file.write(f'{i}\n')

for i in range(10):
    with open('testDEF.txt', ...) as file:
        file.write(f'{i}\n')
```


**20.23.** File objects also have a method `readline`, which does what its name suggests. Use it to print just the first line of a multi-line file. Can you call this method repeatedly to print line after line? (To properly test it, make sure the file you use contains multiple lines of text, like `testABC.txt` written in the previous exercise.)

**20.24.** Instead of calling `read` on a file, or calling `readline` repeatedly, the more Pythonic way is to iterate directly over the file itself. Test the following on a multi-line file, and explain why the resulting printed lines all have empty lines in between. Then tweak the code to prevent this (though if the original file contained an empty line, it should still show up).

```python
with open('testABC.txt', 'r') as file:
    for line in file:
        print(line)
```


**20.25.** What do you expect happens if you duplicate the above loop, such that (within the `with`-statement) it attempts to loop over the file twice? And what if you duplicate the entire `with`-statement (each containing the loop once)? Test your expectations. Does the observed behavior align with what you learned earlier about calling `read` multiple times?


**20.26.** When might it be preferable to read a file one line at a time (which as we have seen can be done by iterating directly over the file object, or with `.readline()`) as opposed to reading the whole file at once? (You can learn more about this in the next, optional section on 'iterators' and 'generators'.)


**20.27.** ⭐⭐ Can you also use _list comprehension_ to iterate over a file? Try this, in order to create (each with a single line within its own `with`-block, to practice): 
 - a list with the first characters of each line in a file. 
 - a list containing all the line lengths. 
 - a list containing the separate lines of the file where each line has been _stripped_ of its final newline character `\n`. 
 - a list of tokenized lines (hence a list of lists). 
 - a list of all lines that begin with a vowel.

**20.28.** What gets printed if you print the file object itself (e.g., `print(file)` instead of `print(file.read())`)? It may say something about an 'encoding'; any idea what that might be?

- - - - - -
**Something to keep in mind:** Each file on your disk is a series of bytes, where each byte is 8 bits (bit = binary digit, i.e, 0 or 1). This is true for text files, but also for images, movies, word documents: they are all just series of bytes. What these bytes _represent_ depends on the **encoding** used for a given file. The default encoding for opening files with Python is `UTF-8` (8-bit Unicode Transformation Format), and you typically don't need to be concerned with this _until it goes wrong_, as we will see.
- - - - -

**20.29.** A simple encoding you may have heard of is ASCII. ASCII represents each character by a single byte. How many distinct characters does ASCII encoding let us represent? Is that enough?

**20.30.** To construct a simple example of 'encodings gone wrong', write some emoji to a file (e.g., 😀😃😄), either with Python or by manual copy-pasting. Emoji (like _many_ characters) are part of the widely adopted _Unicode_ standard, hence available in the default `UTF-8` encoding, but not part of the much smaller ASCII set of characters. Can you open and read this emoji file with Python? What do you expect happens if you give `open` the additional argument `encoding='ASCII'`? Test your expectation.

**20.31.** ⭐ Write a program that takes a path to some file, and replaces all newlines it contains by spaces, overwriting the original file (so be careful what you apply the function to). Can you think of a use-case for this sort of program?


**20.32.** Project Gutenberg (https://www.gutenberg.org/) is an online library of free ebooks, many of which in plain text format. These text files are useful (and potentially interesting) data for some of the quests that follow. Let's download Moby Dick (https://www.gutenberg.org/files/2701/2701-0.txt), and save it to the folder you created earlier for 'files to be analyzed'. You can also download a couple of others. 

**20.33.** Create a function `read_from_gutenberg` for reading Gutenberg-style text files. It should take a path to such a file as input and return the book's text content as a single string. (The books contain some meta-information that you can get rid of in this function, but you can also keep it basic for now. A subsequent Mini-project will ask you to make improvements.) Move your `read_from_gutenberg` function to the file `text_utils.py`, as we will be using it in subsequent sections.




-------

**_Homework exercises for week 11 end here, now do Mini-project [J](../projects/J_implement_the_game_'semantle'.md) (and don't forget to submit! ✉️)._**

-------


**20.34.** ⭐⭐ Write a program (subdivided into functions as you see fit) that takes a path to some input file, opens it and iterates over it to compute some statistics about that file. Compute at least the average number of characters per line, the average number of words per line, and the average number of characters per word. The program should then write these statistics to a new, empty file.


**20.35.** Tweak the foregoing program to ensure that the stats of interest are written to a file that is named after the input file, for instance with `_stats` appended: if the input file is `test123.txt`, the output file could be named `test123_stats.txt`.



**20.36.** ⭐ Create two appropriately named subfolders in your current working directory (or elsewhere): one for the files to be analyzed by your program, and another for the output files (with stats), and adjust the foregoing program accordingly. Why might it be wise (in general) to let your program write files to a new directory, separate from input files, scripts, etc.?






-----

**_🐢 You are now ready for [Mini-project K](../projects/K_processing_some_books.md)!_**

-----

**_🦕 You are now ready for [Mini-project L](../projects/L_scraping_the_web.md)!_**